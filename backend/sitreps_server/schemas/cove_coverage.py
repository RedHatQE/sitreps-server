from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CodeCoverageBase(BaseModel):
    time: Optional[datetime]
    repo_name: Optional[str]  # If multiple repos like backend/frontend
    coverage: float
    # project: instance of Project for relationship
    project_id: Optional[int]


class CodeCoverage(CodeCoverageBase):
    pass


class CodeCoverageCreate(CodeCoverageBase):
    pass


class CodeCoverageUpdate(CodeCoverageBase):
    pass
