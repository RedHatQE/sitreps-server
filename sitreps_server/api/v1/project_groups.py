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
def read_project_groups(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
) -> Any:
    """
    Retrieve Project Groups.
    """
    pg = crud.project_group.get_multi(db, skip=skip, limit=limit)
    return pg


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_project_group(
    *,
    db: Session = Depends(get_db),
    item_in: schemas.ProjectGroupCreate,
) -> Any:
    """
    Create new Project Group.
    """
    pg = crud.project_group.get_with_name(db, name=item_in.name)
    if pg:
        raise HTTPException(
            status_code=status.HTTP_226_IM_USED,
            detail=f"'{item_in.name}' already available.",
        )
    pg = crud.project_group.create(db=db, obj_in=item_in)
    return pg


@router.put("/{id}")
def update_project_group(
    *,
    db: Session = Depends(get_db),
    id: int,
    item_in: schemas.ProjectGroupUpdate,
) -> Any:
    """
    Update an Project Group.
    """
    item = crud.project_group.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Project Group not found")
    item = crud.project_group.update(db=db, db_obj=item, obj_in=item_in)
    return item


@router.get("/{id}")
def read_project_group(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """
    Get Project Group by ID.
    """
    item = crud.project_group.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Project Group not found")
    return item


@router.delete("/{id}")
def delete_project_group(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """
    Delete an Project Group.
    """
    item = crud.project_group.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Project Group not found")
    item = crud.project_group.remove(db=db, id=id)
    return item
