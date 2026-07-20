from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str

    DEBUG: bool = True

    ENVIRONMENT: str

    OLLAMA_BASE_URL: str

    CHAT_MODEL: str

    EMBEDDING_MODEL: str 

    CHROMA_PATH: str

    CHROMA_COLLECTION: str

    UPLOAD_FOLDER: str = "uploads"


    HOST: str
    PORT: str

    LOG_LEVEL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


@lru_cache
def get_settings():
    return Settings()

settings = get_settings()