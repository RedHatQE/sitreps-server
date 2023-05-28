from typing import Any

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from sqlalchemy.orm import Session

from .deps import get_db
from sitreps_server import crud
from sitreps_server import schemas

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_sonarqube(
    *,
    db: Session = Depends(get_db),
    item_in: schemas.SonarQubeCreate,
) -> Any:
    """
    Add new SonarQube Analysis entry.
    """
    item = crud.sonarqube.create(db=db, obj_in=item_in)
    return item


@router.get("/")
async def read_sonarqube(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    filter_by_repository_id: int = None,
) -> Any:
    """
    Retrieve SonarQube data.
    """
    filters = {}
    if filter_by_repository_id:
        filters["repository_id"] = filter_by_repository_id
    item = crud.sonarqube.get_multi(db, skip=skip, limit=limit, filters=filters)
    return item
