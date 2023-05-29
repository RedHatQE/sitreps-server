from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class RequirementsPortalJsonBase(BaseModel):
    time: Optional[datetime]
    data: Optional[dict]


class RequirementsPortalJsonCreate(RequirementsPortalJsonBase):
    pass


class RequirementsPortalJson(RequirementsPortalJsonBase):
    pass


class RequirementsPortalJsonUpdate(RequirementsPortalJsonBase):
    pass


# class RequirementsPortalBase(BaseModel):
#     time: Optional[datetime]

#     plugin: Optional[str]           # Pluign name
#     env: Optional[str]              # Env [prod, stage, fedramp]
#     avg: Optional[str]              # type of avg [core_1, core_7, overall_7]
#     report_time: Optional[str]      # Last analysis time

#     blocked: Optional[float]
#     error: Optional[float]
#     failed: Optional[float]
#     manual: Optional[float]
#     passed: Optional[float]
#     skip: Optional[float]
#     time: Optional[float]
#     xfailed: Optional[float]
#     xpass: Optional[float]


# class RequirementsPortalCreate(RequirementsPortalBase):
#     pass


# class RequirementsPortal(RequirementsPortalBase):
#     pass


# class RequirementsPortalUpdate(RequirementsPortalBase):
#     pass
