from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class RapidastReportBase(BaseModel):
    service: str
    env: Optional[str] = "stage"
    report: Optional[dict]
    html_url: Optional[str]


class RapidastReportCreate(RapidastReportBase):
    pass


class RapidastReport(RapidastReportBase):
    pass


class RapidastReportUpdate(RapidastReportBase):
    pass


class RapidastBase(BaseModel):
    time: Optional[datetime]
    service: str
    service_id: Optional[int] = None
    env: Optional[str] = "stage"
    informational: Optional[int]
    low: Optional[int]
    medium: Optional[int]
    high: Optional[int]
    false_positive: Optional[int]


class RapidastCreate(RapidastBase):
    pass


class Rapidast(RapidastBase):
    pass


class RapidastUpdate(RapidastBase):
    pass
