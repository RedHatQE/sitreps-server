"""Jira schema."""

from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class JiraBase(BaseModel):
    time: datetime | None = None
    project_id: int | None = None  # project: instance of Project for relationship
    project_name: str | None = None  # Jira project id like SPM for patchman
    type: str | None = None  # Type either qe (QE tasks) or dev (Bug against product).

    resolved: int
    jql_resolved: str
    unresolved: int
    jql_unresolved: str
    rejected: int
    jql_rejected: str

    todo: int
    jql_todo: str
    blocked: int
    jql_blocked: str
    in_progress: int
    jql_in_progress: str
    code_review: int
    jql_code_review: str
    on_qa: int
    jql_on_qa: str
    release_pending: int
    jql_release_pending: str

    created_last_15d: int | None = None
    jql_created_last_15d: str | None = None
    created_last_30d: int | None = None
    jql_created_last_30d: str | None = None
    todo_older_than_30d: int | None = None
    jql_todo_older_than_30d: str | None = None
    todo_older_than_60d: int | None = None
    jql_todo_older_than_60d: str | None = None

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
