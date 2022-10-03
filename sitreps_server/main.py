from fastapi import FastAPI
from fastapi.routing import APIRoute


from .api.v1 import api_router
from .core.config import settings
from .db import Base
from .db import engine

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json")
Base.metadata.create_all(engine)

app.include_router(api_router, prefix=settings.API_V1_STR)


def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name  # in this case, 'read_items'


use_route_names_as_operation_ids(app)