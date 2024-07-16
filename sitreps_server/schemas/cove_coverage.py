"""Code coverage schema."""

from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class CodeCoverageBase(BaseModel):
    time: datetime | None = None
    coverage: float
    updatestamp: datetime | None
    line: int | None = None
    hits: int | None = None
    misses: int | None = None
    partials: int | None = None
    # repository: instance of Repository for relationship
    repository_id: int | None = None


class CodeCoverage(CodeCoverageBase):
    model_config = ConfigDict(from_attributes=True)


class CodeCoverageCreate(CodeCoverageBase):
    pass


class CodeCoverageUpdate(CodeCoverageBase):
    pass
