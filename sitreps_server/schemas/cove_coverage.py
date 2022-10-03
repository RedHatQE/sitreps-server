from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CodeCoverageBase(BaseModel):
    time: Optional[datetime]
    coverage: float
    # repository: instance of Repository for relationship
    repository_id: Optional[int]


class CodeCoverage(CodeCoverageBase):
    pass


class CodeCoverageCreate(CodeCoverageBase):
    pass


class CodeCoverageUpdate(CodeCoverageBase):
    pass
