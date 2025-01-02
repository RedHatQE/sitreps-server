"""Unit tests routs."""

from typing import Any

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from sqlalchemy.orm import Session

from sitreps_server import crud
from sitreps_server import schemas

from .deps import get_db

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UnitTestResult)
async def add_unittest_result(
    *,
    db: Session = Depends(get_db),
    item_in: schemas.UnitTestResultCreate,
) -> Any:
    """Add new unittest entry."""
    item = crud.unittest_result.create(db=db, obj_in=item_in)
    return item


@router.get("/", response_model=list[schemas.UnitTestResult])
async def read_unittest_results(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    filter_by_repository_id: int = None,
) -> Any:
    """Retrieve UnitTests data."""
    filters = {}
    if filter_by_repository_id:
        filters["repository_id"] = filter_by_repository_id
    item = crud.unittest_result.get_multi(db, skip=skip, limit=limit, filters=filters)
    return item
