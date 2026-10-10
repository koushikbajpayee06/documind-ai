from langchain_core.documents import Document
from pathlib import Path

import pytest

from app.services import document_service

from app.services.document_service import create_chunks


def test_create_chunks_preserves_page_metadata() -> None:
    documents = [
        Document(
            page_content=(
                "VPN troubleshooting instructions. "
                "Restart the VPN client and check the connection. "
                "Create an IT support ticket if the issue continues."
            ),
            metadata={
                "source": "vpn-guide.pdf",
                "page_number": 4,
            },
        )
    ]

    chunks = create_chunks(
        documents=documents,
        chunk_size=50,
        chunk_overlap=10,
    )

    assert len(chunks) > 1

    for chunk in chunks:
        assert chunk.metadata["source"] == "vpn-guide.pdf"
        assert chunk.metadata["page_number"] == 4

class FakePage:
    def __init__(self, text: str | None) -> None:
        self.text = text

    def extract_text(self) -> str | None:
        return self.text


class FakePdfReader:
    def __init__(self, file_path: Path) -> None:
        self.pages = [
            FakePage("First page content"),
            FakePage("   "),
            FakePage("Third page content"),
        ]

def test_extract_pdf_documents_preserves_page_numbers(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        document_service,
        "PdfReader",
        FakePdfReader,
    )

    documents = document_service.extract_pdf_documents(
        file_path=Path("fake.pdf"),
        source="support-guide.pdf",
    )

    assert len(documents) == 2

    assert documents[0].page_content == "First page content"
    assert documents[0].metadata == {
        "source": "support-guide.pdf",
        "page_number": 1,
    }

    assert documents[1].page_content == "Third page content"
    assert documents[1].metadata == {
        "source": "support-guide.pdf",
        "page_number": 3,
    }

@pytest.mark.parametrize(
    "extension",
    [".txt", ".md"],
)
def test_load_documents_supports_text_files(
    tmp_path: Path,
    extension: str,
) -> None:
    file_path = tmp_path / f"support-notes{extension}"

    file_path.write_text(
        "Restart the VPN client before creating a ticket.",
        encoding="utf-8",
    )

    documents = document_service.load_documents(
        file_path=file_path,
        source=f"support-notes{extension}",
    )

    assert len(documents) == 1
    assert documents[0].page_content == (
        "Restart the VPN client before creating a ticket."
    )
    assert documents[0].metadata == {
        "source": f"support-notes{extension}",
    }