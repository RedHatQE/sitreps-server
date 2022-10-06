from datetime import datetime

from sitreps_server.db import Base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy_json import mutable_json_type
from ..db.types import PortableJSON


class SonarQube(Base):
    """Sonarqube metrics."""

    __tablename__ = "sonarqube"

    time = Column(
        DateTime, default=datetime.utcnow, primary_key=True, index=True
    )  # time for time series data.

    repository_id = Column(Integer, ForeignKey("repositories.id"), index=True)

    project = Column(String)
    vulnerabilities = Column(Integer)
    code_smells = Column(Integer)
    security_hotspots = Column(Integer)
    bugs = Column(Integer)

    # store extra information.
    meta = Column(mutable_json_type(dbtype=PortableJSON()))
