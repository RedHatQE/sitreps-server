"""Code Coverage routs."""

from typing import Any

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from sqlalchemy.orm import Session

from sitreps_server import crud
from sitreps_server import schemas

from .deps import get_db

router = APIRouter()


@router.get("/", response_model=list[schemas.CodeCoverage])
async def read_code_coverage(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    filter_by_repository_id: int = None,
) -> Any:
    """Retrieve items."""
    filters = {}

    if filter_by_repository_id:
        filters["repository_id"] = filter_by_repository_id

    item = crud.code_coverage.get_multi(db, skip=skip, limit=limit, filters=filters)
    return item


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.CodeCoverage)
async def add_code_coverage(
    *,
    db: Session = Depends(get_db),
    item_in: schemas.CodeCoverageCreate,
) -> Any:
    """Create new code coverage entry."""
    item = crud.code_coverage.create(db=db, obj_in=item_in)
    return item
