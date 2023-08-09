from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy_json import mutable_json_type

from ..db.types import PortableJSON
from sitreps_server.db import Base


class RapidastReport(Base):
    """Hold rapiDAST latest report and basic information."""

    __tablename__ = "rapidast_report"

    id = Column(Integer, primary_key=True, index=True)
    service = Column(String)
    env = Column(String)
    report = Column(mutable_json_type(dbtype=PortableJSON(), nested=True))
    html_url = Column(String)


class Rapidast(Base):
    """Rapidast historical data."""

    __tablename__ = "rapidast"

    time = Column(
        DateTime, default=datetime.utcnow, primary_key=True, index=True
    )  # time for time series data.
    service = Column(String)
    service_id = Column(Integer, ForeignKey("rapidast_report.id"), index=True)
    env = Column(String)
    informational = Column(Integer)
    low = Column(Integer)
    medium = Column(Integer)
    high = Column(Integer)
    false_positive = Column(Integer)
