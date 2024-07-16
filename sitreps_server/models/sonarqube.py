"""Sonarqube model."""

from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy_json import mutable_json_type

from sitreps_server.db import Base

from ..db.types import PortableJSON


class SonarQube(Base):
    """Sonarqube metrics."""

    __tablename__ = "sonarqube"

    time = Column(
        DateTime, default=datetime.utcnow, primary_key=True, index=True
    )  # time for time series data.

    repository_id = Column(Integer, ForeignKey("repositories.id"), index=True)

    vulnerabilities = Column(Integer)
    code_smells = Column(Integer)
    security_hotspots = Column(Integer)
    bugs = Column(Integer)
    sonar_last_analysis = Column(DateTime)
    # store extra information.
    meta = Column(mutable_json_type(dbtype=PortableJSON(), nested=True))
