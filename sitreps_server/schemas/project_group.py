"""Project group schema."""

from pydantic import BaseModel
from pydantic import ConfigDict


class ProjectGroupBase(BaseModel):
    name: str


class ProjectGroup(ProjectGroupBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class ProjectGroupCreate(ProjectGroupBase):
    pass


class ProjectGroupUpdate(ProjectGroupBase):
    pass
