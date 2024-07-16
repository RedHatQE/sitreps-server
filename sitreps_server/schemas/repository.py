"""Repository schema."""

from pydantic import BaseModel
from pydantic import ConfigDict


class RepositoryBase(BaseModel):
    name: str
    title: str | None = None
    type: str
    url: str
    maintainer_primary_name: str | None = None
    maintainer_primary_email: str | None = None
    maintainer_secondary_name: str | None = None
    maintainer_secondary_email: str | None = None
    sonarqube_project: str | None = None
    sonarqube_host: str | None = None
    meta: dict | None = None

    project_id: int | None = None


class Repository(RepositoryBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class RepositoryCreate(RepositoryBase):
    pass


class RepositoryUpdate(RepositoryBase):
    name: str | None = None
    type: str | None = None
    url: str | None = None
