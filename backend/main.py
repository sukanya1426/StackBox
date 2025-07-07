# backend/main.py
from fastapi import FastAPI
from app.routers import file_upload, file_download, file_show, file_delete, file_list
from app.utils.db import engine
from app.models.file_metadata import Base
from app.middleware.middleware import setup_cors


app = FastAPI()

# Setup CORS
setup_cors(app)

# Create database tables
Base.metadata.create_all(bind=engine)

app.include_router(file_upload.router)
app.include_router(file_download.router)
app.include_router(file_list.router)
app.include_router(file_show.router)
app.include_router(file_delete.router)

# # Example of a basic root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to StackBox API"}

