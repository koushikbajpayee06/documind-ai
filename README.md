# DocuMind AI

DocuMind AI is a full-stack document intelligence platform that allows users to upload documents and ask context-aware questions using Retrieval-Augmented Generation (RAG).

The system processes documents, generates embeddings, stores them in a vector database, retrieves relevant context, and uses an LLM to produce grounded answers with source references.

## Project Status

🚧 Currently under active development.

The initial project structure and backend environment have been configured. Features will be implemented incrementally.

## Planned Features

- Upload PDF, TXT, and Markdown documents
- Store raw documents locally or in AWS S3
- Extract and chunk document content
- Generate vector embeddings using OpenAI
- Store and retrieve embeddings using ChromaDB
- Ask questions through a conversational interface
- Generate context-aware answers using RAG
- Display source documents and relevant excerpts
- Store document metadata and query history
- Manage indexed documents
- React-based responsive user interface
- FastAPI REST API
- Automated API and service tests
- AWS deployment

## Technology Stack

### Frontend

- React
- Vite
- JavaScript
- CSS

### Backend

- Python
- FastAPI
- Uvicorn
- Pydantic

### AI and Retrieval

- LangChain
- OpenAI
- ChromaDB
- Retrieval-Augmented Generation

### Storage

- SQLite for metadata and logs
- ChromaDB for vector embeddings
- Local storage during development
- AWS S3 for production document storage

## High-Level Architecture

```text
User
  ↓
React Frontend
  ↓
FastAPI Backend
  ├── Document Storage
  ├── Metadata Database
  ├── ChromaDB Vector Store
  ├── OpenAI Embedding Model
  └── OpenAI Chat Model
```

## Document Ingestion Flow

```text
Document Upload
      ↓
FastAPI Backend
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
FastAPI Backend
      ↓
Query Embedding
      ↓
Vector Similarity Search
      ↓
Relevant Document Chunks
      ↓
RAG Prompt
      ↓
Large Language Model
      ↓
Answer with Sources
      ↓
React Frontend
```

## Project Structure

```text
documind-ai/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes/
│   │   ├── models/
│   │   ├── services/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── main.py
│   ├── tests/
│   ├── uploads/
│   ├── vector_db/
│   ├── .env.example
│   ├── .python-version
│   ├── pyproject.toml
│   ├── requirements.txt
│   └── uv.lock
├── frontend/
├── docs/
├── .gitignore
└── README.md
```

## Backend Setup

### 1. Clone the repository

```bash
git clone git@github-koushik:koushikbajpayee06/documind-ai.git
cd documind-ai/backend
```

If the SSH alias is not configured, use the public GitHub URL instead.

### 2. Install dependencies

Using `uv`:

```bash
uv sync
```

Alternatively, using `requirements.txt`:

```bash
python -m venv .venv
```

Activate the environment on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create `backend/.env` using `backend/.env.example` as a reference:

```env
OPENAI_API_KEY=your_openai_api_key

AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
AWS_BUCKET_NAME=your_bucket_name
AWS_REGION=your_aws_region
```

Never commit the `.env` file or expose real credentials publicly.

### 4. Start the FastAPI server

From the `backend` directory:

```bash
uv run uvicorn app.main:app --reload
```

API base URL:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## Frontend Setup

The React frontend will be added in an upcoming milestone.

Once initialized, it will run locally at:

```text
http://localhost:5173
```

## Development Roadmap

- [x] Initialize Git repository
- [x] Set up Python environment with `uv`
- [x] Configure backend dependencies
- [x] Add environment configuration template
- [x] Define initial project architecture
- [ ] Create FastAPI application and health endpoint
- [ ] Initialize React frontend
- [ ] Connect React with FastAPI
- [ ] Implement document upload API
- [ ] Add PDF, TXT, and Markdown parsing
- [ ] Implement document chunking
- [ ] Generate OpenAI embeddings
- [ ] Integrate ChromaDB
- [ ] Build the RAG query pipeline
- [ ] Return answers with source references
- [ ] Add SQLite metadata and chat history
- [ ] Integrate AWS S3
- [ ] Add tests and error handling
- [ ] Containerize the application
- [ ] Deploy the application

## Security

- Secrets are stored using environment variables.
- The `.env` file is excluded from Git.
- Uploaded documents and local vector data are excluded from version control.
- Production credentials must use restricted IAM permissions.
- Raw documents and sensitive information must not be written to application logs.

## License

This project is currently intended for learning and portfolio purposes.