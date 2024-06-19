"""Jira schema."""

from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class JiraBase(BaseModel):
    time: datetime | None = None
    project_id: int | None = None  # project: instance of Project for relationship
    project_name: str | None = None  # Jira project id like SPM for patchman

    resolved: int
    unresolved: int
    rejected: int

    todo: int
    blocked: int
    in_progress: int
    code_review: int
    on_qa: int
    release_pending: int

    created_last_15d: int | None = None
    created_last_30d: int | None = None
    todo_older_than_30d: int | None = None
    todo_older_than_60d: int | None = None

    meta: dict | None = None

    # Future reserved fields.
    jira1: int | None = None
    jira2: int | None = None
    jira3: int | None = None


class Jira(JiraBase):
    model_config = ConfigDict(from_attributes=True)


class JiraCreate(JiraBase):
    pass


class JiraUpdate(JiraBase):
    pass
