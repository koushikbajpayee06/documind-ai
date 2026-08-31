from pathlib import Path
from pypdf import PdfReader

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

SUPPORTED_EXTENSIONS = {".pdf", ".txt", ".md"}


def extract_pdf_text(file_path: Path) -> str:
    reader = PdfReader(file_path)
    extracted_pages = []

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            extracted_pages.append(page_text)

    return "\n".join(extracted_pages)

def extract_text(file_path: str | Path) -> str:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Document not found: {path}")

    extension = path.suffix.lower()

    if extension not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported file type: {extension}")
    if extension in {".txt", ".md"}:
        text = path.read_text(encoding="utf-8")
    else:
        text = extract_pdf_text(path)

    if not text.strip():
        raise ValueError("Document contains no readable text")

    return text

def create_chunks(
    text: str,
    source: str,
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
) -> list[Document]:
    document = Document(
        page_content=text,
        metadata={"source": source},
    )

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    return text_splitter.split_documents([document])