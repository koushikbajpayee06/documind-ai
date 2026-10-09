from functools import lru_cache
from hashlib import sha256

from langchain_chroma import Chroma
from langchain_core.documents import Document

from app.config import settings
from app.services.llm_service import get_embedding_model


@lru_cache
def get_vector_store() -> Chroma:
    return Chroma(
        collection_name=settings.chroma_collection_name,
        embedding_function=get_embedding_model(),
        persist_directory=settings.chroma_persist_dir,
    )

def add_documents_to_vector_store(
    documents: list[Document],
) -> list[str]:
    document_ids = []

    for index, document in enumerate(documents):
        source = document.metadata.get("source", "unknown")

        id_input = (
            f"{source}:{index}:{document.page_content}"
        )

        document_id = sha256(
            id_input.encode("utf-8")
        ).hexdigest()

        document.metadata["chunk_index"] = index
        document.metadata["document_id"] = document_id

        document_ids.append(document_id)

    vector_store = get_vector_store()

    vector_store.add_documents(
        documents=documents,
        ids=document_ids,
    )

    return document_ids

def search_documents(
    query: str,
    number_of_results: int = 4,
) -> list[tuple[Document, float]]:
    if not query.strip():
        raise ValueError("Search query cannot be empty")

    vector_store = get_vector_store()

    document_distance_pairs = vector_store.similarity_search_with_score(
        query=query,
        k=number_of_results,
    )
    return [
        (document, distance)
        for document, distance in document_distance_pairs
        if distance <= settings.max_search_distance
    ]