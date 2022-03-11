from datetime import datetime

from sitreps_server.db import Base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String


class SonarQube(Base):
    """Sonarqube metrics."""

    __tablename__ = "sonarqube"

    time = Column(
        DateTime, default=datetime.utcnow, primary_key=True, index=True
    )  # time for time series data.
    repo_name = Column(String, index=True)  # If multiple then repo name like frontend/backend/tests
    vulnerabilities = Column(Integer, index=True)
    code_smells = Column(Integer, index=True)
    security_hotspots = Column(Integer, index=True)
    bugs = Column(Integer, index=True)

    project_id = Column(Integer, ForeignKey("projects.id"), index=True)
