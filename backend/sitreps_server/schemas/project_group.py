from typing import Optional

from pydantic import BaseModel


class ProjectGroupBase(BaseModel):
    name: str
    title: Optional[str] = None
    description: Optional[str] = None


class ProjectGroup(ProjectGroupBase):
    pass


class ProjectGroupCreate(ProjectGroupBase):
    pass
