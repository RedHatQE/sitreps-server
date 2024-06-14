"""Project group schema."""

from pydantic import BaseModel


class ProjectGroupBase(BaseModel):
    name: str
    title: str | None = None


class ProjectGroup(ProjectGroupBase):
    pass


class ProjectGroupCreate(ProjectGroupBase):
    pass


class ProjectGroupUpdate(ProjectGroupBase):
    pass
