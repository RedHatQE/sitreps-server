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

RISK_MAPPING = {0: "informational", 1: "low", 2: "medium", 3: "high", 4: "false_positive"}


def _extract_data(report):
    data = {}
    data["time"] = report["@generated"]

    site = report["site"][0]
    data["site_name"] = site["@name"]
    data["site_host"] = site["@host"]
    data["site_port"] = site["@port"]
    data["site_ssl"] = site["@ssl"]

    alerts = report["site"][0]["alerts"]
    _alerts_count = {v: 0 for v in RISK_MAPPING.values()}
    for alert in alerts:
        risk_level = RISK_MAPPING[int(alert["riskcode"])]
        _alerts_count[risk_level] += 1
    data.update(_alerts_count)
    return data


@router.put("/", status_code=status.HTTP_201_CREATED)
async def dump_rapidast_report(
    *,
    db: Session = Depends(get_db),
    item_in: schemas.RapidastReport,
) -> Any:
    """
    Update/add rapidast report data.
    """
    service = item_in.service
    env = item_in.env
    # extact data from json to create rapidas schema.
    report_data = _extract_data(report=item_in.report)

    report_item = crud.rapidast_report.get_service_with_name_env(db=db, service=service, env=env)
    if report_item:
        report_item = crud.rapidast_report.update(db=db, db_obj=report_item, obj_in=item_in)
        resp = JSONResponse(
            status_code=200,
            content={"message": f"Rapidas report data for {service} updated successfully."},
        )
    else:
        report_item = crud.rapidast_report.create(db=db, obj_in=item_in)
        resp = report_item

    if report_item:
        rapidas_item_in = schemas.RapidastCreate(
            service=report_item.service,
            service_id=report_item.id,
            env=env,
            informational=report_data.get("informational"),
            low=report_data.get("low"),
            medium=report_data.get("medium"),
            high=report_data.get("high"),
            false_positive=report_data.get("false_positive"),
        )
        crud.rapidast.create(db=db, obj_in=rapidas_item_in)
    return resp


@router.get("/")
async def read_rapidast_report(
    db: Session = Depends(get_db),
    service: str = None,
    env: str = "stage",
) -> Any:
    """
    Retrieve rapidast report.
    """
    if service and env:
        item = crud.rapidast_report.get_service_with_name_env(db=db, service=service, env=env)
        return item
    items = crud.rapidast_report.get_multi(db=db)
    data = []
    for item in items:
        _item = {"name": item.service, "id": item.id, "html_url": item.html_url, "env": item.env}
        report = _extract_data(item.report) if item.report else {}
        _item.update(report)
        data.append(_item)
    if env:
        return [item for item in data if item["env"] == env]
    return data


@router.get("/historical/")
async def read_rapidast(
    db: Session = Depends(get_db),
    service: str = None,
    env: str = "stage",
) -> Any:
    """
    Retrieve rapidast historical data.
    """
    if service and env:
        items = crud.rapidast.get_services_with_name_env(db=db, service=service, env=env)
        return items
    items = crud.rapidast.get_multi(db=db)
    return items
