"""Unittests schema."""

from datetime import datetime

from pydantic import BaseModel


class UnitTestBase(BaseModel):
    time: datetime | None

    # repository: instance of Repository for relationship
    repository_id: int | None

    gh_action: int | None
    jenkins: int | None
    travis: int | None
    other: int | None


class UnitTest(UnitTestBase):
    pass


class UnitTestCreate(UnitTestBase):
    pass


class UnitTestUpdate(UnitTestBase):
    pass
