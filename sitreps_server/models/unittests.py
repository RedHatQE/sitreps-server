from datetime import datetime

from sitreps_server.db import Base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String


class UnitTest(Base):
    """UnitTests for Developement repos."""

    __tablename__ = "unittests"

    time = Column(
        DateTime, default=datetime.utcnow, primary_key=True, index=True
    )  # time for time series data.
    repo_name = Column(String, index=True)  # If multiple then repo name like frontend/backend/tests
    gh_action = Column(Integer, index=True)
    jenkins = Column(Integer, index=True)
    travis = Column(Integer, index=True)

    project_id = Column(Integer, ForeignKey("projects.id"), index=True)
