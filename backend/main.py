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

@app.get("/test-db")
def test_db_connection():
    from sqlalchemy import text
    try:
        # Move this import to the top of the file
        from app.utils.db import DATABASE_URL
        
        # Create a connection
        with engine.connect() as connection:
            # Execute a simple query
            result = connection.execute(text("SELECT 1"))
            # For debugging purposes, print to console
            print("Database connection successful!")
            
            return {
                "status": "success", 
                "message": "Database connection successful", 
                "database_url": DATABASE_URL.replace(":sukanya@", ":****@")  # Hide password in response
            }
    except Exception as e:
        print(f"Database connection error: {str(e)}")
        return {"status": "error", "message": str(e)}