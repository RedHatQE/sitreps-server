"""Unit-tests model."""

from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

from sitreps_server.db import Base


class UnitTest(Base):
    """UnitTests for Developement repos."""

    __tablename__ = "unittests"

    time = Column(
        DateTime, default=datetime.utcnow, primary_key=True, index=True
    )  # time for time series data.

    repository_id = Column(Integer, ForeignKey("repositories.id"), index=True)

    gh_action = Column(Integer)
    jenkins = Column(Integer)
    travis = Column(Integer)
    other = Column(Integer)
