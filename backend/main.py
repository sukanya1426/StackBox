# backend/main.py
from fastapi import FastAPI
from routers import file_upload
from utils.db import engine
from models.file_metadata import Base

app = FastAPI()

# Include your routers
Base.metadata.create_all(bind=engine)
app.include_router(file_upload.router)
