from pathlib import Path
from pypdf import PdfReader

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

SUPPORTED_EXTENSIONS = {".pdf", ".txt", ".md"}


def extract_pdf_documents(
    file_path: Path,
    source: str,
) -> list[Document]:
    reader = PdfReader(file_path)
    documents = []

    for page_number, page in enumerate(
        reader.pages,
        start=1,
    ):
        page_text = page.extract_text()

        if page_text and page_text.strip():
            documents.append(
                Document(
                    page_content=page_text,
                    metadata={
                        "source": source,
                        "page_number": page_number,
                    },
                )
            )

    return documents

def load_documents(
    file_path: str | Path,
    source: str,
) -> list[Document]:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Document not found: {path}")

    extension = path.suffix.lower()

    if extension not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported file type: {extension}")

    if extension == ".pdf":
        documents = extract_pdf_documents(
            file_path=path,
            source=source,
        )
    else:
        text = path.read_text(encoding="utf-8")

        documents = [
            Document(
                page_content=text,
                metadata={
                    "source": source,
                },
            )
        ]

    if not documents or not any(
        document.page_content.strip()
        for document in documents
    ):
        raise ValueError("Document contains no readable text")

    return documents

def create_chunks(
    documents: list[Document],
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
) -> list[Document]:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    return text_splitter.split_documents(documents)