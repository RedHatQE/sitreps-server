from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CLOCBase(BaseModel):
    time: Optional[datetime]
    repo_name: Optional[str]  # If multiple repos like backend/frontend
    cloc: int
    # project: instance of Project for relationship
    project_id: Optional[int]


class CLOC(CLOCBase):
    pass


class CLOCCreate(CLOCBase):
    pass


class CLOCUpdate(CLOCBase):
    pass
