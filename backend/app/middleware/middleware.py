from fastapi.middleware.cors import CORSMiddleware

def setup_cors(app):
    """
    Set up CORS middleware for the FastAPI app.
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000"],  # Frontend URL
        allow_credentials=True,
        allow_methods=["*"],  # Allow all methods (GET, POST, DELETE, etc.)
        allow_headers=["*"],  # Allow all headers
    )