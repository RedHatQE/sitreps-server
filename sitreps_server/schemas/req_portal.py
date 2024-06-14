"""Req-portal schema."""

from datetime import datetime

from pydantic import BaseModel


class RequirementsPortalJsonBase(BaseModel):
    time: datetime | None
    data: list | None


class RequirementsPortalJsonCreate(RequirementsPortalJsonBase):
    pass


class RequirementsPortalJson(RequirementsPortalJsonBase):
    pass


class RequirementsPortalJsonUpdate(RequirementsPortalJsonBase):
    pass


class RequirementsPortalBase(BaseModel):
    time: datetime | None

    plugin: str | None  # Pluign name
    env: str | None  # Env [prod, stage, fedramp]
    avg: str | None  # type of avg [core_1, core_7, overall_7]
    report_time: str | None  # Last analysis time

    blocked: float | None
    error: float | None
    failed: float | None
    manual: float | None
    passed: float | None
    skip: float | None
    xfailed: float | None
    xpass: float | None


class RequirementsPortalCreate(RequirementsPortalBase):
    pass


class RequirementsPortal(RequirementsPortalBase):
    pass


class RequirementsPortalUpdate(RequirementsPortalBase):
    pass
