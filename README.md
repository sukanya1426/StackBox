# StackBox - File Storage Platform

A modern, full-stack file storage and management platform built with **Next.js** frontend, **FastAPI** backend, **PostgreSQL** database, and **Azure Blob Storage** for file storage.

## 🚀 Features

- **File Upload & Download**: Secure file upload with support for multiple file types
- **File Management**: View, download, and delete files with an intuitive dashboard
- **Cloud Storage**: Files are stored in Azure Blob Storage with SAS token authentication
- **Modern UI**: Responsive design built with Tailwind CSS and React
- **Database Integration**: PostgreSQL database for file metadata management
- **Containerized**: Full Docker support for easy deployment
- **API Documentation**: FastAPI automatic API documentation
- **File Metadata**: Track file size, type, upload date, and more

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Next.js       │    │   FastAPI       │    │   PostgreSQL    │
│   Frontend      │◄──►│   Backend       │◄──►│   Database      │
│   (Port 3000)   │    │   (Port 8000)   │    │   (Port 5432)   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │ Azure Blob      │
                       │ Storage         │
                       └─────────────────┘
```

- **Nginx** - Reverse proxy (optional)

## 📋 Prerequisites

- Docker and Docker Compose
- Azure Storage Account
- Git

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/StackBox.git
cd StackBox
```

### 2. Environment Configuration

Create environment files:

**Backend (.env)**

```bash
# Database
DATABASE_URL=postgresql://postgres:sukanya@postgres:5432/stackbox

# Azure Storage
AZURE_STORAGE_CONN_STR=your_azure_connection_string
AZURE_CONTAINER_NAME=stackbox
AZURE_ACCOUNT_NAME=your_account_name
AZURE_ACCOUNT_KEY=your_account_key
```

**Frontend (.env)**

```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### 3. Start with Docker Compose

```bash
# Build and start all services
docker-compose up -d

# View logs
docker-compose logs -f
```

### 4. Access the Application

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 🔧 Development Setup

### Local Development (without Docker)

#### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

#### Database Setup

```bash
# Install PostgreSQL locally or use Docker
docker run --name postgres -e POSTGRES_PASSWORD=sukanya -p 5432:5432 -d postgres:15-alpine
```

## 📚 API Endpoints

| Method | Endpoint               | Description       |
| ------ | ---------------------- | ----------------- |
| GET    | `/`                    | API health check  |
| POST   | `/upload`              | Upload a file     |
| GET    | `/list-files`          | Get all files     |
| GET    | `/download/{filename}` | Download a file   |
| GET    | `/show/{filename}`     | Get file metadata |
| DELETE | `/delete/{filename}`   | Delete a file     |

## 🐳 Docker Configuration

The project includes multi-container setup:

- **Frontend**: Next.js app (Port 3000)
- **Backend**: FastAPI app (Port 8000)
- **Database**: PostgreSQL (Port 5432)
- **Nginx**: Reverse proxy (Port 80) - Optional

## 🔄 CI/CD Pipeline

GitHub Actions workflows included:

- **Code Linting**: Automated code quality checks
- **EC2 Deployment**: Deployment to AWS EC2 instances

## 🛡️ Security Features

- **CORS Configuration**: Secure cross-origin requests
- **SAS Tokens**: Temporary access to Azure Blob Storage
- **Input Validation**: File type and size restrictions
- **SQL Injection Protection**: SQLAlchemy ORM protection

## 📱 Features in Detail

### File Upload

- Drag-and-drop interface
- Progress indicators
- File type validation
- Size limitations (configurable)

### File Management

- Grid and list view options
- File search and filtering
- Bulk operations
- File preview (for supported types)

### Storage Management

- Automatic file organization
- Duplicate detection
- Storage usage tracking
- Cleanup utilities

## 🚀 Deployment

### Production Deployment

1. **Environment Variables**: Set production environment variables
2. **SSL Certificates**: Configure HTTPS with Let's Encrypt
3. **Database**: Use managed PostgreSQL service
4. **Monitoring**: Set up application monitoring
5. **Backup**: Configure regular backups

### Scaling Considerations

- Load balancing with multiple backend instances
- Database connection pooling
- CDN for static assets
- Horizontal scaling with Kubernetes

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
