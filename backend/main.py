# backend/main.py
from fastapi import FastAPI
from app.routers import file_upload, file_download , file_show, file_delete
from app.utils.db import engine
from app.models.file_metadata import Base

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

app.include_router(file_upload.router)
app.include_router(file_download.router)
app.include_router(file_show.router)
app.include_router(file_delete.router)