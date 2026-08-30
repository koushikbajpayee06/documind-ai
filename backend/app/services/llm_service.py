from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from app.config import settings


def get_chat_model() -> ChatOpenAI:
    return ChatOpenAI(
        model=settings.openai_chat_model,
        temperature=settings.openai_temperature,
        api_key=settings.openai_api_key.get_secret_value(),
    )


def get_embedding_model() -> OpenAIEmbeddings:
    return OpenAIEmbeddings(
        model=settings.openai_embedding_model,
        api_key=settings.openai_api_key.get_secret_value(),
    )