from datetime import datetime

from sitreps_server.db import Base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer


class SonarQube(Base):
    """Sonarqube metrics."""

    __tablename__ = "sonarqube"

    time = Column(
        DateTime, default=datetime.utcnow, primary_key=True, index=True
    )  # time for time series data.
    vulnerabilities = Column(Integer, index=True)
    code_smells = Column(Integer, index=True)
    security_hotspots = Column(Integer, index=True)
    bugs = Column(Integer, index=True)

    repository_id = Column(Integer, ForeignKey("repositories.id"), index=True)
