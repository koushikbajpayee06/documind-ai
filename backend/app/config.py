from functools import lru_cache
from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

BACKEND_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    # OpenAI settings
    openai_api_key: SecretStr
    openai_chat_model: str = "gpt-4o-mini"
    openai_embedding_model: str = "text-embedding-3-small"
    openai_temperature: float = 0.0

    # AWS settings — optional until S3 integration is implemented
    aws_access_key_id: SecretStr | None = None
    aws_secret_access_key: SecretStr | None = None
    aws_bucket_name: str | None = None
    aws_region: str = "ap-south-1"

    upload_dir: Path = BACKEND_DIR / "uploads"
    max_upload_size_mb: int = 10

    frontend_url: str = "http://localhost:5173"

    # ChromaDB settings
    chroma_persist_dir: Path = BACKEND_DIR / "vector_db"
    chroma_collection_name: str = "documind_documents"
    max_search_distance: float = 1.25

    model_config = SettingsConfigDict(
        env_file=BACKEND_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()