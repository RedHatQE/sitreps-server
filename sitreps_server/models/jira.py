from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy_json import mutable_json_type

from ..db.types import PortableJSON
from sitreps_server.db import Base


class Jira(Base):
    """Table hold jira data."""

    __tablename__ = "jira"

    time = Column(
        DateTime, default=datetime.utcnow, primary_key=True, index=True
    )  # time for time series data.

    project_id = Column(Integer, ForeignKey("projects.id"), index=True)
    project_name = Column(String, index=True)  # Jira project name

    resolved = Column(Integer, index=True)
    unresolved = Column(Integer, index=True)
    rejected = Column(Integer, index=True)

    todo = Column(Integer, index=True)
    blocked = Column(Integer, index=True)
    in_progress = Column(Integer, index=True)
    code_review = Column(Integer, index=True)
    on_qa = Column(Integer, index=True)
    release_pending = Column(Integer, index=True)

    created_last_15d = Column(Integer, index=True)
    created_last_30d = Column(Integer, index=True)

    todo_older_than_30d = Column(Integer, index=True)
    todo_older_than_60d = Column(Integer, index=True)

    # JQL/URL meta
    meta = Column(mutable_json_type(dbtype=PortableJSON(), nested=True))

    # Extra filed reserved for future
    jira1 = Column(Integer, index=True)
    jira2 = Column(Integer, index=True)
    jira3 = Column(Integer, index=True)
