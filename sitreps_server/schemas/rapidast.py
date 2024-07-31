"""Rapidast schema."""

from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class RapidastReportBase(BaseModel):
    service: str
    plugin_name: str
    env: str | None = "stage"
    report: dict | None = None
    html_url: str | None = None


class RapidastReportCreate(RapidastReportBase):
    pass


class RapidastReport(RapidastReportBase):
    model_config = ConfigDict(from_attributes=True)


class RapidastReportUpdate(RapidastReportBase):
    pass


class RapidastBase(BaseModel):
    time: datetime | None = None
    service: str
    service_id: int | None = None
    env: str | None = "stage"
    informational: int | None = None
    low: int | None = None
    medium: int | None = None
    high: int | None = None
    false_positive: int | None = None


class RapidastCreate(RapidastBase):
    pass


class Rapidast(RapidastBase):
    pass


class RapidastUpdate(RapidastBase):
    pass
