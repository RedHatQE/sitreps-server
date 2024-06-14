"""Code coverage schema."""

from datetime import datetime

from pydantic import BaseModel


class CodeCoverageBase(BaseModel):
    time: datetime | None
    coverage: float
    # repository: instance of Repository for relationship
    repository_id: int | None


class CodeCoverage(CodeCoverageBase):
    pass


class CodeCoverageCreate(CodeCoverageBase):
    pass


class CodeCoverageUpdate(CodeCoverageBase):
    pass
