from typing import Any

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from .deps import get_db
from sitreps_server import crud
from sitreps_server import schemas

router = APIRouter()


@router.get("/")
def read_repositories(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
    filter_by_project_id: int = None,
    filter_by_type: str = None,
) -> Any:
    """
    Retrieve Repositories data.
    """
    filters = {}

    if filter_by_project_id:
        filters["project_id"] = filter_by_project_id
    if filter_by_type:
        filters["type"] = filter_by_type

    repo = crud.repository.get_multi(db, skip=skip, limit=limit, filters=filters)
    return repo


@router.get("/{id}")
def read_repository_id(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """
    Get Repository by ID.
    """
    item = crud.repository.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="repository not found")
    return item


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_repository(
    *,
    db: Session = Depends(get_db),
    item_in: schemas.RepositoryCreate,
) -> Any:
    """
    Create new item.
    """
    repo = crud.repository.get_with_name(db, name=item_in.name)
    if repo:
        raise HTTPException(
            status_code=status.HTTP_226_IM_USED,
            detail=f"'{item_in.name}' already available.",
        )
    repo = crud.repository.create(db=db, obj_in=item_in)
    return repo


@router.put("/{id}")
def update_repository(
    *,
    db: Session = Depends(get_db),
    id: int,
    item_in: schemas.RepositoryUpdate,
) -> Any:
    """
    Update an item.
    """
    item = crud.repository.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="repository not found")
    item = crud.repository.update(db=db, db_obj=item, obj_in=item_in)
    return item


@router.delete("/{id}")
def delete_repository(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """
    Delete an item.
    """
    item = crud.repository.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="repository not found")
    item = crud.repository.remove(db=db, id=id)
    return item
