from typing import Optional

from pydantic import BaseModel


class ProjectBase(BaseModel):
    name: str
    title: Optional[str] = None
    # group: instance of ProjectGroup for relation
    group_id: Optional[int] = None


class Project(ProjectBase):
    pass


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(ProjectBase):
    pass
