"""Req-portal routs."""

from logging import getLogger
from typing import Any

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from sitreps_server import crud
from sitreps_server import schemas

from .deps import get_db

router = APIRouter()
LOGGER = getLogger(__name__)


@router.put("/latest/", status_code=status.HTTP_201_CREATED)
async def dump_requirements_portal_raw_data(
    *,
    db: Session = Depends(get_db),
    item_in: schemas.RequirementsPortalJson,
) -> Any:
    """Update/add requirements portal avg json data."""
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


@router.get("/latest/")
async def read_requirements_portal_raw_data(
    db: Session = Depends(get_db),
    filter_by_plugin: str = None,
    filter_by_env: str = None,
    filter_by_avg: str = None,
) -> Any:
    """Retrieve requinments portal avg json data."""
    item = crud.req_portal_json.get_first(db=db)
    if item:
        data = item.data
        if filter_by_plugin:
            data = [i for i in data if i["plugin"] == filter_by_plugin]
        if filter_by_env:
            data = [i for i in data if i["env"] == filter_by_env]
        if filter_by_avg:
            data = [i for i in data if i["avg"] == filter_by_avg]
        return data
    return item


@router.get("/pass_rate/")
async def read_services_passing_rate(
    db: Session = Depends(get_db),
    filter_by_env: str = "prod",
    filter_by_avg: str = "core-7",
) -> Any:
    """Retrieve services passing rate."""
    item = crud.req_portal_json.get_first(db=db)
    if item:
        _item = {}
        _frontend_plugins = []
        _missing_mapping = []
        for plugin in item.data:
            if plugin["env"] == filter_by_env and plugin["avg"] == filter_by_avg:
                plugin_name = plugin["plugin"]
                if "frontend" in plugin_name:
                    # For now we are skipping frontend plugins.
                    # We need to decide about taking average of frontend and backend.
                    _frontend_plugins.append(plugin_name)
                    continue
                service = plugin["service"]
                if service:
                    _item.update({service: plugin["passed"]})
                else:
                    _missing_mapping.append(plugin_name)
        print(f"Service mapping missing following plugins: \n \n {set(_missing_mapping)} \n")
        print(f"Skipping those frontend pugins: \n \n {set(_frontend_plugins)} \n")
        return _item
    return item


@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_historical_average(
    *,
    db: Session = Depends(get_db),
    item_in: schemas.RequirementsPortalCreate,
) -> Any:
    """Add new requirements portal avg entry."""
    existing_item = crud.req_portal.get_last_req_portal_avg(
        db=db, plugin=item_in.plugin, avg=item_in.avg, env=item_in.env
    )
    if existing_item and item_in.time.date() == existing_item.time.date():
        item = crud.req_portal.update(db=db, db_obj=existing_item, obj_in=item_in)
        return JSONResponse(
            status_code=200,
            content={
                "message": f"Requirements portal data for {item_in.plugin} updated successfully"
            },
        )
    else:
        item = crud.req_portal.create(db=db, obj_in=item_in)
        return item


@router.get("/")
async def read_historical_average(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    filter_by_plugin: str = None,
    filter_by_env: str = None,
    filter_by_avg: str = None,
) -> Any:
    """Retrieve requinment portal avg data."""
    filters = {}
    if filter_by_plugin:
        filters["plugin"] = filter_by_plugin
    if filter_by_env:
        filters["env"] = filter_by_env
    if filter_by_avg:
        filters["avg"] = filter_by_avg
    item = crud.req_portal.get_multi(db, skip=skip, limit=limit, filters=filters)
    return item
