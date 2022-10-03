from datetime import datetime

from sitreps_server.db import Base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String


class CodeCoverage(Base):
    """Code Coverage."""

    __tablename__ = "codecoverage"

    time = Column(
        DateTime, default=datetime.utcnow, primary_key=True, index=True
    )  # time for time series data.
    coverage = Column(Float, index=True)

    repository_id = Column(Integer, ForeignKey("repositories.id"), index=True)
