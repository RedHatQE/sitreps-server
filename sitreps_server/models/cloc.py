from datetime import datetime

from sitreps_server.db import Base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String


class CLOC(Base):
    """Count Line of Code."""

    __tablename__ = "cloc"

    time = Column(
        DateTime, default=datetime.utcnow, primary_key=True, index=True
    )  # time for time series data.
    repo_name = Column(String, index=True)  # If multiple then repo name like frontend/backend/tests
    cloc = Column(Integer, index=True)

    project_id = Column(Integer, ForeignKey("projects.id"), index=True)
