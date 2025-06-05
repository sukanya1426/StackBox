from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from app.utils.db import get_db
from app.models.file_metadata import FileMetadata
from sqlalchemy.orm import Session
import requests

router = APIRouter()

@router.get("/download/{filename}")
async def download_file(filename: str, db: Session = Depends(get_db)):
    # Query the database for a file with the matching filename
    file_metadata = db.query(FileMetadata).filter(FileMetadata.filename == filename).first()
    
    # If no file is found, raise a 404 error
    if not file_metadata:
        raise HTTPException(status_code=404, detail=f"File '{filename}' not found")
    
  
    sas_url = file_metadata.blob_url
    print(f"Attempting to fetch file from SAS URL: {sas_url}")
    
  
    try:
        response = requests.get(sas_url, stream=True)
        response.raise_for_status()  # Raises an exception for 4xx/5xx status codes
        print(f"Fetch successful, status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching file: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to fetch file from Azure Blob Storage: {str(e)}")
    
    # Stream the file back to the user with the original filename
    headers = {
        "Content-Disposition": f"attachment; filename={file_metadata.filename}",
        "Content-Type": file_metadata.content_type or "application/octet-stream"
    }
    
    def file_stream():
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                yield chunk
        response.close()
    
    return StreamingResponse(file_stream(), headers=headers)