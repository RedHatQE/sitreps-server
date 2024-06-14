"""Jira routs."""

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
async def add_jira(
    *,
    db: Session = Depends(get_db),
    item_in: schemas.JiraCreate,
) -> Any:
    """Add new Jira entry."""
    item = crud.jira.create(db=db, obj_in=item_in)
    return item


@router.get("/")
async def read_jira(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    filter_by_project_id: int = None,
    filter_by_project_name: str = None,
) -> Any:
    """Retrieve Jira data."""
    filters = {}

    if filter_by_project_id:
        filters["project_id"] = filter_by_project_id

    if filter_by_project_name:
        filters["project_name"] = filter_by_project_name

    item = crud.jira.get_multi(db, skip=skip, limit=limit, filters=filters)
    return item


@router.get("/{project_id}")
async def read_latest_meta(
    project_id: int,
    db: Session = Depends(get_db),
) -> Any:
    """Retrieve latest Jira 'meta' field for Project."""
    item = crud.jira.get_last_with_project_id(db, project_id=project_id)
    return item.meta if item else {}
