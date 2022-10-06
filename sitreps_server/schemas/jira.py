from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class JiraBase(BaseModel):
    time: Optional[datetime]
    project_id: Optional[int]       # project: instance of Project for relationship
    project_name: Optional[str]     # Jira project id like SPM for patchman

    resolved: int
    unresolved: int
    rejected: int

    todo: int
    blocked: int
    in_progress: int
    code_review: int
    on_qa: int

    created_last_15d: Optional[int]
    created_last_30d: Optional[int]
    todo_older_than_30d: Optional[int]
    todo_older_than_60d: Optional[int]

    meta: Optional[dict]

    # Future reserved fields.
    jira1: Optional[int]
    jira2: Optional[int]
    jira3: Optional[int]


class Jira(JiraBase):
    pass


class JiraCreate(JiraBase):
    pass


class JiraUpdate(JiraBase):
    pass
