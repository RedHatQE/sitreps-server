"""Configuration for sitreps backend."""

from functools import lru_cache
from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

BASE_PATH = Path(__file__).resolve().parent.parent


class AppConfig(BaseModel):
    """Application configurations."""

    BASE_DIR: Path = BASE_PATH


class GlobalConfig(BaseSettings):
    """Global configurations."""

    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "sitreps"

    POSTGRESQL_SERVER: str = "localhost"
    POSTGRESQL_PORT: int = 5432
    POSTGRESQL_DATABASE: str = "sitreps"
    POSTGRESQL_USER: str = "admin"
    POSTGRESQL_PASSWORD: str = "admin"
    DATABASE_URL: str = ""
    model_config = SettingsConfigDict(
        case_sensitive=True, env_file=BASE_PATH.parent / ".env", extra="allow"
    )


# for avoid multiple calls.
@lru_cache
def get_settings():
    """Get configurations."""
    return GlobalConfig()


settings = get_settings()
