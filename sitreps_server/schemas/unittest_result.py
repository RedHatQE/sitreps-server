"""Unittests schema."""

from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class UnitTestResultBase(BaseModel):
    time: datetime | None = None

    # repository: instance of Repository for relationship
    repository_id: int | None = None

    ci_name: str
    framework_name: str
    passed: int = 0
    failed: int = 0
    skipped: int = 0
    total: int = 0


class UnitTestResult(UnitTestResultBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class UnitTestResultCreate(UnitTestResultBase):
    pass


class UnitTestResultUpdate(UnitTestResultBase):
    pass
