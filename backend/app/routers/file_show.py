from fastapi import APIRouter, Depends, HTTPException
from app.utils.db import get_db
from app.models.file_metadata import FileMetadata
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/show/{filename}")
async def show_file(filename: str, db: Session = Depends(get_db)):
    file_metadata = db.query(FileMetadata).filter(FileMetadata.filename == filename).first()
    
   
    if not file_metadata:
        raise HTTPException(status_code=404, detail=f"File '{filename}' not found")
    
    # Return the blob URL for the file
    return {"message": "File found", "url": file_metadata.blob_url}