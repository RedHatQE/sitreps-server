"""Project schema."""

from pydantic import BaseModel
from pydantic import ConfigDict


class ProjectBase(BaseModel):
    name: str
    title: str | None = None
    # group: instance of ProjectGroup for relation
    group_id: int | None = None

    # Hold some extra info
    meta: dict | None = None


class Project(ProjectBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(ProjectBase):
    pass
