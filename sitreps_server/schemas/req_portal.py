"""Req-portal schema."""

from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class RequirementsPortalJsonBase(BaseModel):
    time: datetime | None = None
    data: list | None = None


class RequirementsPortalJsonCreate(RequirementsPortalJsonBase):
    pass


class RequirementsPortalJson(RequirementsPortalJsonBase):
    model_config = ConfigDict(from_attributes=True)


class RequirementsPortalJsonUpdate(RequirementsPortalJsonBase):
    pass


class RequirementsPortalBase(BaseModel):
    time: datetime | None = None

    plugin: str | None = None  # Pluign name
    env: str | None = None  # Env [prod, stage, fedramp]
    avg: str | None = None  # type of avg [core_1, core_7, overall_7]
    report_time: datetime | None = None  # Last analysis time

    blocked: float | None = None
    error: float | None = None
    failed: float | None = None
    manual: float | None = None
    passed: float | None = None
    skip: float | None = None
    xfailed: float | None = None
    xpass: float | None = None


class RequirementsPortalCreate(RequirementsPortalBase):
    pass


class RequirementsPortal(RequirementsPortalBase):
    model_config = ConfigDict(from_attributes=True)


class RequirementsPortalUpdate(RequirementsPortalBase):
    pass
