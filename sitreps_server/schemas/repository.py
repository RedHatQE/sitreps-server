"""Repository schema."""

from pydantic import BaseModel
from pydantic import ConfigDict


class RepositoryBase(BaseModel):
    name: str
    title: str | None = None
    type: str
    url: str
    sonar_last_analysis: str = None
    meta: dict | None = None

    project_id: int | None = None


class Repository(RepositoryBase):
    model_config = ConfigDict(from_attributes=True)


class RepositoryCreate(RepositoryBase):
    pass


class RepositoryUpdate(RepositoryBase):
    pass
