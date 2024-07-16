"""Project schema."""

from pydantic import BaseModel
from pydantic import ConfigDict


class ProjectBase(BaseModel):
    name: str | None = None
    title: str | None = None
    manager_name: str | None = None
    manager_email: str | None = None
    # group: instance of ProjectGroup for relation
    group_id: int | None = None

    # Hold some extra info
    meta: dict | None = None


class Project(ProjectBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class ProjectCreate(ProjectBase):
    name: str


class ProjectUpdate(ProjectBase):
    pass
