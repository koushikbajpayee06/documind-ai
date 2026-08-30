# DocuMind AI

DocuMind AI is a full-stack document intelligence platform that allows users to upload documents and ask context-aware questions using Retrieval-Augmented Generation (RAG).

The system processes documents, generates embeddings, stores them in a vector database, retrieves relevant context, and uses a Large Language Model (LLM) to produce grounded answers with source references.

## Project Status

🚧 Currently under active development.

The React frontend and FastAPI backend are successfully connected. Users can upload PDF, TXT, and Markdown documents through the React interface, with file validation and local backend storage.

## Planned Features

- Upload PDF, TXT, and Markdown documents
- Store raw documents locally or in AWS S3
- Extract and chunk document content
- Generate vector embeddings using OpenAI
- Store and retrieve embeddings using ChromaDB
- Ask questions through a conversational interface
- Generate context-aware answers using RAG
- Display source documents and relevant excerpts
- Store document metadata and conversation history
- Resume previous conversations
- Manage indexed documents
- Provide a responsive React interface
- Expose REST APIs using FastAPI
- Add automated API and service tests
- Deploy the application on AWS

## Technology Stack

### Frontend

- React
- Vite
- JavaScript
- CSS
- Fetch API

### Backend

- Python
- FastAPI
- Uvicorn
- Pydantic
- Pydantic Settings

### AI and Retrieval

- LangChain
- OpenAI
- ChromaDB
- Retrieval-Augmented Generation

### Storage

- SQLite for metadata, logs, and conversation history
- ChromaDB for vector embeddings
- Local storage during development
- AWS S3 for production document storage

### Development Tools

- uv
- npm
- Git
- GitHub
- Swagger UI

## High-Level Architecture

```text
End User
    ↓
React Frontend
    ↓
FastAPI Backend
    ├── Document Storage
    ├── Metadata Database
    ├── Conversation History
    ├── ChromaDB Vector Store
    ├── OpenAI Embedding Model
    └── OpenAI Chat Model
```

## Document Ingestion Flow

```text
Document Upload
      ↓
React Frontend
      ↓
FastAPI Backend
      ↓
File Validation
      ↓
Document Storage
      ↓
Document Parsing
      ↓
Text Chunking
      ↓
Embedding Generation
      ↓
ChromaDB Vector Store
```

## RAG Query Flow

```text
User Question
      ↓
React Frontend
      ↓
FastAPI Backend
      ↓
Load Conversation History
      ↓
Generate Query Embedding
      ↓
Vector Similarity Search
      ↓
Retrieve Relevant Chunks
      ↓
Build RAG Prompt
      ↓
OpenAI Chat Model
      ↓
Answer with Sources
      ↓
Save Conversation
      ↓
React Frontend
```

## Project Structure

```text
documind-ai/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── routes/
│   │   │       ├── __init__.py
│   │   │       ├── documents.py
│   │   │       └── health.py
│   │   ├── models/
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   └── document.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── llm_service.py
│   │   │   └── storage_service.py
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── main.py
│   ├── tests/
│   ├── uploads/
│   │   └── .gitkeep
│   ├── vector_db/
│   │   └── .gitkeep
│   ├── .env.example
│   ├── .python-version
│   ├── pyproject.toml
│   ├── requirements.txt
│   └── uv.lock
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   │   └── DocumentUpload.jsx
│   │   ├── App.css
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   ├── .env.example
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.js
├── docs/
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

Make sure the following tools are installed:

- Python 3.10 or later
- uv
- Node.js
- npm
- Git

## Clone the Repository

Using HTTPS:

```bash
git clone https://github.com/koushikbajpayee06/documind-ai.git
cd documind-ai
```

Using SSH:

```bash
git clone git@github.com:koushikbajpayee06/documind-ai.git
cd documind-ai
```

## Backend Setup

### 1. Navigate to the backend

```bash
cd backend
```

### 2. Install dependencies

Using `uv`:

```bash
uv sync
```

Alternatively, create a standard virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure backend environment variables

Create `backend/.env` using `backend/.env.example`:

```env
OPENAI_API_KEY=your_openai_api_key
OPENAI_CHAT_MODEL=gpt-4o-mini
OPENAI_EMBEDDING_MODEL=text-embedding-3-small
OPENAI_TEMPERATURE=0

AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
AWS_BUCKET_NAME=your_bucket_name
AWS_REGION=ap-south-1

FRONTEND_URL=http://localhost:5173

UPLOAD_DIR=uploads
MAX_UPLOAD_SIZE_MB=10

CHROMA_PERSIST_DIR=vector_db
CHROMA_COLLECTION_NAME=documind_documents
DATABASE_URL=sqlite:///./documind.db
```

Never commit the `.env` file or expose real credentials publicly.

### 4. Start the FastAPI server

From the `backend` directory:

```bash
uv run uvicorn app.main:app --reload
```

Backend links:

- API: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Health check: [http://127.0.0.1:8000/api/health](http://127.0.0.1:8000/api/health)
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Expected health-check response:

```json
{
  "status": "healthy",
  "message": "DocuMind AI API is running"
}
```

## Frontend Setup

### 1. Navigate to the frontend

Open another terminal from the project root:

```bash
cd frontend
```

### 2. Install dependencies

```bash
npm install
```

### 3. Configure frontend environment variables

Create `frontend/.env` using `frontend/.env.example`:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

### 4. Start the React development server

```bash
npm run dev
```

The frontend will be available at:

[http://localhost:5173](http://localhost:5173)

When both servers are running, the frontend should display:

```text
Backend status: DocuMind AI API is running
```

## Document Upload

Users can upload documents from the React interface.

Supported file formats:

- PDF
- TXT
- Markdown

Maximum file size:

```text
10 MB
```

Upload endpoint:

```text
POST /api/documents/upload
```

Successful response:

```json
{
  "message": "Document uploaded successfully",
  "original_filename": "example.pdf",
  "stored_filename": "generated-uuid.pdf",
  "content_type": "application/pdf",
  "size_bytes": 12345
}
```

Uploaded files are assigned UUID-based filenames to prevent collisions and are stored locally inside `backend/uploads/` during development.

## Development Roadmap

- [x] Initialize Git repository
- [x] Set up Python environment with `uv`
- [x] Configure backend dependencies
- [x] Add environment configuration templates
- [x] Define initial project architecture
- [x] Configure OpenAI chat and embedding models
- [x] Create FastAPI application and health endpoint
- [x] Initialize React frontend
- [x] Configure CORS
- [x] Connect React with FastAPI
- [x] Implement document upload API
- [x] Build the React document-upload interface
- [x] Connect document upload interface with FastAPI
- [x] Add file type and size validation
- [ ] Add PDF, TXT, and Markdown parsing
- [ ] Implement document chunking
- [ ] Generate document embeddings
- [ ] Integrate ChromaDB
- [ ] Build the history-aware RAG pipeline
- [ ] Return answers with source references
- [ ] Add SQLite metadata and conversation history
- [ ] Add conversation resume functionality
- [ ] Integrate AWS S3
- [ ] Add automated tests and error handling
- [ ] Containerize the application
- [ ] Deploy the application

## Security

- Secrets are stored using environment variables.
- Sensitive values are handled using Pydantic `SecretStr`.
- Backend and frontend `.env` files are excluded from Git.
- Uploaded documents and local vector data are excluded from version control.
- Uploaded files are validated by extension and size.
- UUID-based stored filenames help prevent filename collisions.
- Production AWS credentials should use restricted IAM permissions.
- Raw documents and sensitive information should not be written to application logs.

## Author

**Koushik Bajpayee**

- GitHub: [koushikbajpayee06](https://github.com/koushikbajpayee06)

## License

This project is currently intended for learning and portfolio purposes.