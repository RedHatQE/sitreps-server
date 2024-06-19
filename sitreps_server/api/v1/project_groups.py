"""Project group routs."""

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


@router.get("/", response_model=list[schemas.ProjectGroup])
async def read_project_groups(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
) -> Any:
    """Retrieve Project Groups."""
    pg = crud.project_group.get_multi(db, skip=skip, limit=limit)
    return pg
    # import ipdb; ipdb.set_trace()
    # return [schemas.ProjectGroup.from_orm(g) for g in pg]
    # return pg


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ProjectGroup)
async def create_project_group(
    *,
    db: Session = Depends(get_db),
    item_in: schemas.ProjectGroupCreate,
) -> Any:
    """Create new Project Group."""
    pg = crud.project_group.get_with_name(db, name=item_in.name)
    if pg:
        raise HTTPException(
            status_code=status.HTTP_226_IM_USED,
            detail=f"'{item_in.name}' already available.",
        )
    pg = crud.project_group.create(db=db, obj_in=item_in)
    return pg


@router.put("/{id}", response_model=schemas.ProjectGroup)
async def update_project_group(
    *,
    db: Session = Depends(get_db),
    id: int,
    item_in: schemas.ProjectGroupUpdate,
) -> Any:
    """Update an Project Group."""
    item = crud.project_group.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Project Group not found")
    item = crud.project_group.update(db=db, db_obj=item, obj_in=item_in)
    return item


@router.get("/{id}", response_model=schemas.ProjectGroup)
async def read_project_group(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """Get Project Group by ID."""
    item = crud.project_group.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Project Group not found")
    return item


@router.delete("/{id}", response_model=schemas.ProjectGroup)
async def delete_project_group(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """Delete an Project Group."""
    item = crud.project_group.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="Project Group not found")
    item = crud.project_group.remove(db=db, id=id)
    return item
