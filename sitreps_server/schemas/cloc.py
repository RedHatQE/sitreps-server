from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CLOCBase(BaseModel):
    time: Optional[datetime]
    cloc: int
    meta: Optional[dict]
    # repository: instance of Repository for relationship
    repository_id: Optional[int]


class CLOC(CLOCBase):
    pass


class CLOCCreate(CLOCBase):
    pass


class CLOCUpdate(CLOCBase):
    pass
