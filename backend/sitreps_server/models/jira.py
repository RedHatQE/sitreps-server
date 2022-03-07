from datetime import datetime

from sitreps_server.db import Base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String


class Jira(Base):
    """Table hold jira data."""

    __tablename__ = "jira"

    time = Column(
        DateTime, default=datetime.utcnow, primary_key=True, index=True
    )  # time for time series data.
    project_name = Column(String, index=True)  # Jira project name
    todo = Column(Integer, index=True)
    in_progress = Column(Integer, index=True)
    code_review = Column(Integer, index=True)
    blocked = Column(Integer, index=True)
    on_qa = Column(Integer, index=True)
    unresolved = Column(Integer, index=True)
    resolved = Column(Integer, index=True)
    rejected = Column(Integer, index=True)
    created_last_month = Column(Integer, index=True)
    resolved_last_month = Column(Integer, index=True)
    todo_older_than_60d = Column(Integer, index=True)

    project_id = Column(Integer, ForeignKey("projects.id"), index=True)
