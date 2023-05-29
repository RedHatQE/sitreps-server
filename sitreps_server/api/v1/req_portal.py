from logging import getLogger
from typing import Any

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from .deps import get_db
from sitreps_server import crud
from sitreps_server import schemas


router = APIRouter()
LOGGER = getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def dump_requirements_portal_avg_json(
    *,
    db: Session = Depends(get_db),
    item_in: schemas.RequirementsPortalJson,
) -> Any:
    """
    Update/add requirements portal avg json data.
    """
    item = crud.req_portal_json.get_first(db=db)
    if item:
        item = crud.req_portal_json.update(db=db, db_obj=item, obj_in=item_in)
        return JSONResponse(
            status_code=200,
            content={"message": "Requirements portal avg json data updated successfully."},
        )
    else:
        item = crud.req_portal_json.create(db=db, obj_in=item_in)
    return item


@router.get("/")
async def read_requirements_portal_avg_json(
    db: Session = Depends(get_db),
) -> Any:
    """
    Retrieve requinments portal avg json data.
    """
    item = crud.req_portal_json.get_first(db=db)
    return item.data
