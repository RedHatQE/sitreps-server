from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UnitTestBase(BaseModel):
    time: Optional[datetime]
    gh_action: int
    jenkins: int
    travis: int
    # repository: instance of Repository for relationship
    repository_id: Optional[int]


class UnitTest(UnitTestBase):
    pass


class UnitTestCreate(UnitTestBase):
    pass


class UnitTestUpdate(UnitTestBase):
    pass
