"""CLOC schema."""

from datetime import datetime

from pydantic import BaseModel


class CLOCBase(BaseModel):
    time: datetime | None
    cloc: int
    meta: dict | None
    # repository: instance of Repository for relationship
    repository_id: int | None


class CLOC(CLOCBase):
    pass


class CLOCCreate(CLOCBase):
    pass


class CLOCUpdate(CLOCBase):
    pass
