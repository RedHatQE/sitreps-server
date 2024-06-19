"""Unittests schema."""

from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class UnitTestBase(BaseModel):
    time: datetime | None = None

    # repository: instance of Repository for relationship
    repository_id: int | None = None

    gh_action: int | None = None
    jenkins: int | None = None
    travis: int | None = None
    other: int | None = None


class UnitTest(UnitTestBase):
    model_config = ConfigDict(from_attributes=True)


class UnitTestCreate(UnitTestBase):
    pass


class UnitTestUpdate(UnitTestBase):
    pass
