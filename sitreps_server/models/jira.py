"""Jira model."""

from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy_json import mutable_json_type

from sitreps_server.db import Base

from ..db.types import PortableJSON


class Jira(Base):
    """Table hold jira data."""

    __tablename__ = "jira"

    time = Column(
        DateTime, default=datetime.utcnow, primary_key=True, index=True
    )  # time for time series data.

    project_id = Column(Integer, ForeignKey("projects.id"), index=True)
    project_name = Column(String, index=True)  # Jira project name
    # Type either qe (QE tasks) or dev (Bug against product).
    type = Column(String, index=True)

    resolved = Column(Integer)
    jql_resolved = Column(String)
    unresolved = Column(Integer)
    jql_unresolved = Column(String)
    rejected = Column(Integer)
    jql_rejected = Column(String)

    todo = Column(Integer)
    jql_todo = Column(String)

    blocked = Column(Integer)
    jql_blocked = Column(String)
    in_progress = Column(Integer)
    jql_in_progress = Column(String)
    code_review = Column(Integer)
    jql_code_review = Column(String)
    on_qa = Column(Integer)
    jql_on_qa = Column(String)
    release_pending = Column(Integer)
    jql_release_pending = Column(String)

    created_last_15d = Column(Integer)
    jql_created_last_15d = Column(String)
    created_last_30d = Column(Integer)
    jql_created_last_30d = Column(String)

    todo_older_than_30d = Column(Integer)
    jql_todo_older_than_30d = Column(String)
    todo_older_than_60d = Column(Integer)
    jql_todo_older_than_60d = Column(String)

    # JQL/URL meta
    meta = Column(mutable_json_type(dbtype=PortableJSON(), nested=True))

    # Extra filed reserved for future
    jira1 = Column(Integer, index=True)
    jira2 = Column(Integer, index=True)
    jira3 = Column(Integer, index=True)
