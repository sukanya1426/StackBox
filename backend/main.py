# backend/main.py
from fastapi import FastAPI
from app.routers import file_upload
from app.utils.db import engine
from app.models.file_metadata import Base

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include your routers
app.include_router(file_upload.router)