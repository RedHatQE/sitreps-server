"""Repository schema."""

from pydantic import BaseModel


class RepositoryBase(BaseModel):
    name: str
    title: str | None = None
    type: str
    url: str
    sonar_last_analysis: str = None
    meta: dict | None = None

    project_id: int | None = None


class Repository(RepositoryBase):
    pass


class RepositoryCreate(RepositoryBase):
    pass


class RepositoryUpdate(RepositoryBase):
    pass
