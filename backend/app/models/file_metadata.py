from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class FileMetadata(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    content_type = Column(String)
    size = Column(Integer)
    blob_name = Column(String)  # Store the blob name separately
    blob_url = Column(String)
    uploaded_at = Column(DateTime, default=datetime.utcnow)
