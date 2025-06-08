# StackBox File Manager

Welcome to StackBox, a full-stack file management application built with a Next.js frontend, a FastAPI backend, PostgreSQL for data storage, and Nginx as a reverse proxy. This project allows users to upload, download, list, and delete files, with file storage handled via Azure Blob Storage and metadata stored in PostgreSQL.

This project allows users to upload, download, list, and delete files. File contents are stored in Azure Blob Storage, while file metadata is managed via PostgreSQL.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/stackbox.git
cd stackbox
docker-compose up --build
