from fastapi import APIRouter, Depends
from app.utils.db import get_db
from app.models.file_metadata import FileMetadata
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/list-files")
async def list_files(db: Session = Depends(get_db)):
    # Fetch all files, ordered by upload date descending
    files = db.query(FileMetadata).order_by(FileMetadata.uploaded_at.desc()).all()
    return files