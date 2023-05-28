from typing import Optional

from pydantic import BaseModel


class RepositoryBase(BaseModel):
    name: str
    title: Optional[str] = None
    type: str
    url: str
    sonar_last_analysis: str = None
    meta: Optional[dict] = None

    project_id: Optional[int] = None


class Repository(RepositoryBase):
    pass


class RepositoryCreate(RepositoryBase):
    pass


class RepositoryUpdate(RepositoryBase):
    pass
