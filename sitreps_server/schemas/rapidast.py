"""Rapidast schema."""

from datetime import datetime

from pydantic import BaseModel


class RapidastReportBase(BaseModel):
    service: str
    plugin_name: str = None
    env: str | None = "stage"
    report: dict | None
    html_url: str | None


class RapidastReportCreate(RapidastReportBase):
    pass


class RapidastReport(RapidastReportBase):
    pass


class RapidastReportUpdate(RapidastReportBase):
    pass


class RapidastBase(BaseModel):
    time: datetime | None
    service: str
    service_id: int | None = None
    env: str | None = "stage"
    informational: int | None
    low: int | None
    medium: int | None
    high: int | None
    false_positive: int | None


class RapidastCreate(RapidastBase):
    pass


class Rapidast(RapidastBase):
    pass


class RapidastUpdate(RapidastBase):
    pass
