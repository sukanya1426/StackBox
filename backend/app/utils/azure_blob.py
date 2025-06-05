from azure.storage.blob import BlobServiceClient, generate_blob_sas
from azure.storage.blob import BlobSasPermissions
from datetime import datetime, timedelta
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
    
    # Generate SAS token with 1-hour expiration
    sas_token = generate_blob_sas(
        account_name=blob_client.account_name,
        container_name=container,
        blob_name=blob_name,
        account_key=blob_service.credential.account_key,
        permission=BlobSasPermissions(read=True),
        expiry=datetime.utcnow() + timedelta(days=365*100)
    )
    
    # Construct the SAS URL
    sas_url = f"{blob_client.url}?{sas_token}"
    return blob_name, sas_url