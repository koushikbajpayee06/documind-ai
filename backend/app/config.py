
from functools import lru_cache
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    openai_api_key: SecretStr
    openai_chat_model: str = "gpt-4o-mini"
    openai_embedding_model: str = "text-embedding-3-small"
    openai_temperature: float = 0.0

    aws_access_key: SecretStr
    aws_secret_key: SecretStr
    aws_bucket_name: str
    aws_region: str = "ap-south-1"

    frontend_url: str = "http://localhost:5173"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()