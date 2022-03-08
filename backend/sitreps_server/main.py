from fastapi import FastAPI

from .api.v1 import api_router
from .core.config import settings
from .db import Base
from .db import engine

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json")
Base.metadata.create_all(engine)

app.include_router(api_router, prefix=settings.API_V1_STR)
