from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UnitTestBase(BaseModel):
    time: Optional[datetime]
    repo_name: Optional[str]  # If multiple repos like backend/frontend
    gh_action: int
    jenkins: int
    travis: int
    # project: instance of Project for relationship
    project_id: Optional[int]


class UnitTest(UnitTestBase):
    pass


class UnitTestCreate(UnitTestBase):
    pass
