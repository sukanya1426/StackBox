# backend/main.py
from fastapi import FastAPI
from routers import file_upload

app = FastAPI()

# Include your routers
app.include_router(file_upload.router)
