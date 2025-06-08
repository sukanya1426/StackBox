# StackBox File Manager

Welcome to StackBox, a full-stack file management application built with a Next.js frontend, a FastAPI backend, PostgreSQL for data storage, and Nginx as a reverse proxy. This project allows users to upload, download, list, and delete files, with file storage handled via Azure Blob Storage and metadata stored in PostgreSQL.

This project allows users to upload, download, list, and delete files. File contents are stored in Azure Blob Storage, while file metadata is managed via PostgreSQL.

---

##  Getting Started

## 1. Clone the Repository 

```bash
git clone https://github.com/your-username/stackbox.git
cd stackbox
docker-compose up --build
```
## 2. Start Docker
```bash
docker-compose up --build
```
This command will:

-  **Build** the frontend and backend images
-  **Start** PostgreSQL and initialize the `stackbox` database
-  **Launch** the FastAPI backend at [http://localhost:8000](http://localhost:8000)
-  **Run** the Next.js frontend at [http://localhost:3000](http://localhost:3000)
-  **Route traffic via Nginx**:
  - `/` → Frontend  
  - `/api/` → Backend
