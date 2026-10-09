import pytest
from langchain_core.documents import Document

from app.services import vector_store

class FakeVectorStore:
    def similarity_search_with_score(
        self,
        query: str,
        k: int,
    ) -> list[tuple[Document, float]]:
        return [
            (
                Document(
                    page_content="Relevant VPN instructions",
                    metadata={"source": "vpn.txt"},
                ),
                0.80,
            ),
            (
                Document(
                    page_content="Irrelevant cooking instructions",
                    metadata={"source": "cooking.txt"},
                ),
                1.60,
            ),
        ]
    

def test_search_documents_filters_results_above_max_distance(
    monkeypatch,
) -> None:
    fake_vector_store = FakeVectorStore()

    monkeypatch.setattr(
        vector_store,
        "get_vector_store",
        lambda: fake_vector_store,
    )
    monkeypatch.setattr(
        vector_store.settings,
        "max_search_distance",
        1.25,
    )

    results = vector_store.search_documents(
        query="VPN problem",
        number_of_results=2,
    )

    assert len(results) == 1

    document, distance = results[0]

    assert document.page_content == "Relevant VPN instructions"
    assert document.metadata["source"] == "vpn.txt"
    assert distance == 0.80


def test_search_documents_rejects_empty_query() -> None:
    with pytest.raises(
        ValueError,
        match="Search query cannot be empty",
    ):
        vector_store.search_documents(query="   ")


def test_search_documents_returns_empty_when_all_results_are_too_far(
    monkeypatch,
) -> None:
    fake_vector_store = FakeVectorStore()

    monkeypatch.setattr(
        vector_store,
        "get_vector_store",
        lambda: fake_vector_store,
    )
    monkeypatch.setattr(
        vector_store.settings,
        "max_search_distance",
        0.50,
    )

    results = vector_store.search_documents(
        query="unrelated question",
        number_of_results=2,
    )

    assert results == []