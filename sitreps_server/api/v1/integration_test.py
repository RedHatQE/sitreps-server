"""Integration tests routs."""

from typing import Any

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from sqlalchemy.orm import Session

from sitreps_server import crud
from sitreps_server import schemas

from .deps import get_db

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_integration_test(
    *,
    db: Session = Depends(get_db),
    item_in: schemas.IntegrationTestCreate,
) -> Any:
    """Create new item."""
    item = crud.integration_test.create(db=db, obj_in=item_in)
    return item


@router.get("/")
async def read_integration_test(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    filter_by_repository_id: int = None,
) -> Any:
    """Retrieve integration tests entries."""
    filters = {}

    if filter_by_repository_id:
        filters["repository_id"] = filter_by_repository_id

    item = crud.integration_test.get_multi(db, skip=skip, limit=limit, filters=filters)
    return item
