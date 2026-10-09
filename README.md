# DocuMind AI — Enterprise IT Support Assistant

DocuMind AI is a full-stack document intelligence platform that allows users to upload documents and retrieve context-aware information using Retrieval-Augmented Generation (RAG).

The system extracts content from uploaded documents, splits it into searchable chunks, generates vector embeddings, stores them in ChromaDB, and performs semantic similarity searches to retrieve relevant document sections.

## Project Status

🚧 Currently under active development.

The following features are currently working:

- React frontend connected with FastAPI
- PDF, TXT, and Markdown document uploads
- File type and size validation
- Local document storage with UUID-based filenames
- Text extraction from supported documents
- Recursive document chunking
- OpenAI embedding generation
- Persistent ChromaDB vector storage
- Duplicate-safe document indexing
- Semantic similarity search API

The next milestone is building the RAG question-answering pipeline using the retrieved document chunks and the OpenAI chat model.

## Features

### Implemented

- Upload PDF, TXT, and Markdown documents
- Validate uploaded file type and size
- Store uploaded documents locally
- Extract readable text from documents
- Split documents into overlapping chunks
- Generate embeddings using OpenAI
- Persist embeddings in ChromaDB
- Prevent duplicate chunk indexing using deterministic IDs
- Perform semantic similarity searches
- Display upload and processing results in React
- Expose REST APIs using FastAPI
- Provide interactive API documentation through Swagger UI

### Planned

- Generate grounded answers using RAG
- Display source documents and relevant excerpts
- Build a React question-answering interface
- Store document metadata in SQLite
- Store conversation history
- Resume previous conversations
- Manage indexed documents
- Store production documents in AWS S3
- Add automated API and service tests
- Containerize and deploy the application

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
- Recursive Character Text Splitter

### Document Processing

- PyPDF
- Pathlib
- LangChain Documents

### Storage

- ChromaDB for vector embeddings
- Local filesystem during development
- SQLite for planned metadata and conversation history
- AWS S3 for planned production document storage

### Development Tools

- uv
- npm
- Git
- GitHub
- Swagger UI

## High-Level Architecture

```text
End User
    │
    ▼
React Frontend
    │
    ▼
FastAPI Backend
    ├── Document Validation
    ├── Local Document Storage
    ├── Document Processing
    ├── OpenAI Embedding Model
    ├── ChromaDB Vector Store
    └── OpenAI Chat Model (RAG milestone)
```

## Document Ingestion Flow

```text
Document Upload
      │
      ▼
React Frontend
      │
      ▼
FastAPI Upload API
      │
      ▼
File Validation
      │
      ▼
Local Document Storage
      │
      ▼
Text Extraction
      │
      ▼
Recursive Text Chunking
      │
      ▼
OpenAI Embedding Generation
      │
      ▼
ChromaDB Vector Store
```

## Semantic Search Flow

```text
Search Query
      │
      ▼
FastAPI Semantic Search API
      │
      ▼
OpenAI Query Embedding
      │
      ▼
ChromaDB Similarity Search
      │
      ▼
Relevant Document Chunks
      │
      ▼
JSON Response with Sources
```

## Planned RAG Flow

```text
User Question
      │
      ▼
React Frontend
      │
      ▼
FastAPI Backend
      │
      ▼
Load Conversation History
      │
      ▼
Semantic Similarity Search
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Build RAG Prompt
      │
      ▼
OpenAI Chat Model
      │
      ▼
Answer with Sources
      │
      ▼
Save Conversation
      │
      ▼
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
│   │   │       ├── health.py
│   │   │       └── search.py
│   │   │
│   │   ├── models/
│   │   │
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── document.py
│   │   │   └── search.py
│   │   │
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── document_service.py
│   │   │   ├── llm_service.py
│   │   │   ├── storage_service.py
│   │   │   └── vector_store.py
│   │   │
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── main.py
│   │
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
│
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
│
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

### 1. Navigate to the Backend

```bash
cd backend
```

### 2. Install Dependencies

Using `uv`:

```bash
uv sync
```

Alternatively, create a standard Python virtual environment:

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

### 3. Configure Backend Environment Variables

Create `backend/.env` using `backend/.env.example` as a reference:

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

### 4. Start the FastAPI Server

From the `backend` directory:

```bash
uv run uvicorn app.main:app --reload
```

Backend links:

- API: http://127.0.0.1:8000
- Health check: http://127.0.0.1:8000/api/health
- Swagger UI: http://127.0.0.1:8000/docs

Expected health-check response:

```json
{
  "status": "healthy",
  "message": "DocuMind AI API is running"
}
```

## Frontend Setup

### 1. Navigate to the Frontend

Open another terminal from the project root:

```bash
cd frontend
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Configure Frontend Environment Variables

Create `frontend/.env` using `frontend/.env.example` as a reference:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

### 4. Start the React Development Server

```bash
npm run dev
```

The frontend will be available at:

```text
http://localhost:5173
```

When both servers are running, the frontend should display:

```text
Backend status: DocuMind AI API is running
```

## Document Upload

Users can upload documents from the React interface.

Supported formats:

- PDF
- TXT
- Markdown

Maximum file size:

```text
10 MB
```

### Upload Endpoint

```http
POST /api/documents/upload
```

The request must use `multipart/form-data` with a field named `file`.

Example successful response:

```json
{
  "message": "Document uploaded, processed, and indexed successfully",
  "original_filename": "example.pdf",
  "stored_filename": "generated-uuid.pdf",
  "content_type": "application/pdf",
  "size_bytes": 587379,
  "character_count": 110399,
  "chunk_count": 138
}
```

During document upload, the backend:

1. Validates the file type and size.
2. Assigns a UUID-based stored filename.
3. Saves the document inside `backend/uploads/`.
4. Extracts readable text from the document.
5. Divides the text into overlapping chunks.
6. Generates embeddings for each chunk.
7. Stores the chunks and embeddings in ChromaDB.

## Semantic Search

The semantic search endpoint retrieves document chunks that are conceptually related to the provided query.

### Search Endpoint

```http
POST /api/search/semantic
```

Example request:

```json
{
  "query": "What are the benefits of APIs?",
  "number_of_results": 3
}
```

Example response:

```json
{
  "query": "What are the benefits of APIs?",
  "results": [
    {
      "content": "APIs enable different systems and applications to communicate...",
      "metadata": {
        "source": "Complete Notes.pdf",
        "chunk_index": 1,
        "document_id": "generated-deterministic-id"
      }
    }
  ]
}
```

The search endpoint currently returns relevant chunks. Answer generation using the retrieved context will be added in the RAG milestone.

## Duplicate-Safe Indexing

DocuMind AI generates deterministic identifiers for document chunks using their source, chunk index, and content.

This prevents the same chunk from being stored repeatedly when an identical document is uploaded more than once.

## Current Development Status

The current application supports local document upload, persistent ChromaDB indexing, and semantic search through both the FastAPI API and React interface.

RAG answer generation, source citations, conversation history, authentication, ticket workflows, and production deployment have not yet been implemented.

## Development Roadmap

- [x] Initialize Git repository
- [x] Set up Python environment with `uv`
- [x] Configure backend dependencies
- [x] Add environment configuration templates
- [x] Define the initial project architecture
- [x] Configure OpenAI chat and embedding models
- [x] Create the FastAPI application and health endpoint
- [x] Initialize the React frontend
- [x] Configure CORS
- [x] Connect React with FastAPI
- [x] Implement the document upload API
- [x] Build the React document-upload interface
- [x] Add file type and size validation
- [x] Add PDF, TXT, and Markdown parsing
- [x] Implement recursive document chunking
- [x] Generate document embeddings
- [x] Integrate persistent ChromaDB storage
- [x] Add duplicate-safe chunk indexing
- [x] Implement the semantic similarity search API
- [x] Build the React semantic-search interface
- [ ] Build the history-aware RAG pipeline
- [ ] Return generated answers with source references
- [ ] Add SQLite metadata and conversation history
- [ ] Add conversation resume functionality
- [ ] Add indexed-document management
- [ ] Integrate AWS S3
- [ ] Add automated tests and improved error handling
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
- OpenAI and AWS credentials must never be committed to Git.

## Author

**Koushik Bajpayee**

- GitHub: [koushikbajpayee06](https://github.com/koushikbajpayee06)

## License

This project is currently intended for learning and portfolio purposes.
