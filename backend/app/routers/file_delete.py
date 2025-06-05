from fastapi import APIRouter, Depends, HTTPException
from app.utils.db import get_db
from app.models.file_metadata import FileMetadata
from sqlalchemy.orm import Session
from azure.storage.blob import BlobServiceClient
import os
from dotenv import load_dotenv

router = APIRouter()

# Load environment variables
load_dotenv()
conn_str = os.getenv("AZURE_STORAGE_CONN_STR")
container = os.getenv("AZURE_CONTAINER_NAME")
blob_service = BlobServiceClient.from_connection_string(conn_str)
container_client = blob_service.get_container_client(container)

@router.delete("/delete/{filename}")
async def delete_file(filename: str, db: Session = Depends(get_db)):
    # Query the database for the latest file with the matching filename
    file_metadata = db.query(FileMetadata).filter(FileMetadata.filename == filename)\
                    .order_by(FileMetadata.uploaded_at.desc()).first()
    
    # If no file is found, raise a 404 error
    if not file_metadata:
        raise HTTPException(status_code=404, detail=f"File '{filename}' not found")
    
    # Extract the blob name from the blob_url
    blob_url = file_metadata.blob_url
    if "?" in blob_url:
        blob_name = blob_url.split("?")[0].split(f"{container}/")[-1]
    else:
        blob_name = blob_url.split(f"{container}/")[-1]
    
    # Delete the blob from Azure Blob Storage
    blob_client = container_client.get_blob_client(blob_name)
    try:
        blob_client.delete_blob()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete file from Azure Blob Storage: {str(e)}")
    
    # Delete the file metadata from the database
    db.delete(file_metadata)
    db.commit()
    
    return {"message": f"File '{filename}' deleted successfully"}