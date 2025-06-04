from azure.storage.blob import BlobServiceClient
import os
from uuid import uuid4
from dotenv import load_dotenv

load_dotenv()
conn_str = os.getenv("AZURE_STORAGE_CONN_STR")
container = os.getenv("AZURE_CONTAINER_NAME")

blob_service = BlobServiceClient.from_connection_string(conn_str)
container_client = blob_service.get_container_client(container)

def upload_to_blob(file):
    blob_name = f"{uuid4()}_{file.filename}"
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(file.file, overwrite=True)
    return blob_client.url
