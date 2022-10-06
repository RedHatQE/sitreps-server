from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UnitTestBase(BaseModel):
    time: Optional[datetime]

    # repository: instance of Repository for relationship
    repository_id: Optional[int]

    gh_action: Optional[int]
    jenkins: Optional[int]
    travis: Optional[int]
    other: Optional[int]

class UnitTest(UnitTestBase):
    pass


class UnitTestCreate(UnitTestBase):
    pass


class UnitTestUpdate(UnitTestBase):
    pass
