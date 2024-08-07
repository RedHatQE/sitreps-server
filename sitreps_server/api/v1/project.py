"""Project routs."""

from typing import Any

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from sitreps_server import crud
from sitreps_server import schemas

from .deps import get_db

router = APIRouter()


@router.get("/", response_model=list[schemas.Project])
async def read_projects(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
) -> Any:
    """Retrieve Projects."""
    proj = crud.project.get_multi(db, skip=skip, limit=limit)
    return proj


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Project)
async def create_project(
    *,
    db: Session = Depends(get_db),
    item_in: schemas.ProjectCreate,
) -> Any:
    """Create new Project."""
    proj = crud.project.get_with_name(db, name=item_in.name)
    if proj:
        raise HTTPException(
            status_code=status.HTTP_226_IM_USED,
            detail=f"'{item_in.name}' already available.",
        )
    proj = crud.project.create(db=db, obj_in=item_in)
    return proj


@router.put("/{id}", response_model=schemas.Project)
async def update_project(
    *,
    db: Session = Depends(get_db),
    id: int,
    item_in: schemas.ProjectUpdate,
) -> Any:
    """Update an Project."""
    item = crud.project.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Project Group not found")
    item = crud.project.update(db=db, db_obj=item, obj_in=item_in)
    return item


@router.get("/{id}", response_model=schemas.Project)
async def read_project_id(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """Get project by ID."""
    item = crud.project.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Project Group not found")
    return item


@router.delete("/{id}", response_model=schemas.Project)
async def delete_project(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """Delete an project."""
    item = crud.project.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Project Group not found")
    item = crud.project.remove(db=db, id=id)
    return item
