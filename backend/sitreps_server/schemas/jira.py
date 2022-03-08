from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class JiraBase(BaseModel):
    time: Optional[datetime]
    project_name: Optional[str]  # Jira project id like SPM for patchman
    todo: int
    in_progress: int
    code_review: int
    blocked: int
    on_qa: int
    unresolved: int
    resolved: int
    rejected: int
    created_last_month: Optional[int]
    resolved_last_month: Optional[int]
    todo_older_than_60d: Optional[int]

    # project: instance of Project for relationship
    project_id: Optional[int]


class Jira(JiraBase):
    pass


class JiraCreate(JiraBase):
    pass


class JiraUpdate(JiraBase):
    pass
