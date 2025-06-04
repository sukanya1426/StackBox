from fastapi import APIRouter, File, UploadFile, Depends
from app.utils.azure_blob import upload_to_blob
from app.utils.db import get_db
from app.models.file_metadata import FileMetadata
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await file.read()
    size = len(contents)
    # Reset file pointer for upload_to_blob
    file.file.seek(0)
    blob_url = upload_to_blob(file)
    metadata = FileMetadata(
        filename=file.filename,
        content_type=file.content_type,
        size=size,
        blob_url=blob_url
    )
    print(metadata)
    print("File uploaded to blob storage:", blob_url)
    db.add(metadata)
    db.commit()
    db.refresh(metadata)
    return {"message": "File uploaded", "url": blob_url}