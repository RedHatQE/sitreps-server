from functools import lru_cache
from pathlib import Path

from pydantic import BaseModel
from pydantic import BaseSettings


class AppConfig(BaseModel):
    """Application configurations."""

    BASE_DIR: Path = Path(__file__).resolve().parent.parent


class GlobalConfig(BaseSettings):
    """Global configurations."""

    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "sitreps"

    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "sitreps"
    POSTGRES_USER: str = "admin"
    POSTGRES_PASSWORD: str = "admin"

    class Config:
        case_sensitive = True
        env_file = ".env"


# for avoid multiple calls.
@lru_cache()
def get_settings():
    return GlobalConfig()


settings = get_settings()
