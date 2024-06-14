"""Jira schema."""

from datetime import datetime

from pydantic import BaseModel


class JiraBase(BaseModel):
    time: datetime | None
    project_id: int | None  # project: instance of Project for relationship
    project_name: str | None  # Jira project id like SPM for patchman

    resolved: int
    unresolved: int
    rejected: int

    todo: int
    blocked: int
    in_progress: int
    code_review: int
    on_qa: int
    release_pending: int

    created_last_15d: int | None
    created_last_30d: int | None
    todo_older_than_30d: int | None
    todo_older_than_60d: int | None

    meta: dict | None

    # Future reserved fields.
    jira1: int | None
    jira2: int | None
    jira3: int | None


class Jira(JiraBase):
    pass


class JiraCreate(JiraBase):
    pass


class JiraUpdate(JiraBase):
    pass
