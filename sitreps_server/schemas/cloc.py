"""CLOC schema."""

from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class CLOCBase(BaseModel):
    time: datetime | None = None
    cloc: int
    meta: dict | None = None
    # repository: instance of Repository for relationship
    repository_id: int | None = None


class CLOC(CLOCBase):
    model_config = ConfigDict(from_attributes=True)


class CLOCCreate(CLOCBase):
    pass


class CLOCUpdate(CLOCBase):
    pass
