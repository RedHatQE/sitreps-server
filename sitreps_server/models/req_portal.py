"""Req-portal model."""

from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy_json import mutable_json_type

from sitreps_server.db import Base

from ..db.types import PortableJSON


class RequirementsPortalJson(Base):
    """Hold requirements portal avg data in json for all env and plugins."""

    __tablename__ = "req_portal_latest"

    time = Column(
        DateTime, default=datetime.utcnow, primary_key=True, index=True
    )  # Just for primary key at we are not going to use it.
    data = Column(mutable_json_type(dbtype=PortableJSON(), nested=True))


class RequirementsPortal(Base):
    """Requirements portal historical data."""

    __tablename__ = "req_portal"

    time = Column(
        DateTime, default=datetime.utcnow, primary_key=True, index=True
    )  # time for time series data.
    plugin = Column(String, index=True)
    env = Column(String, index=True)
    avg = Column(String, index=True)
    report_time = Column(DateTime, index=True)

    blocked = Column(Float)
    error = Column(Float)
    failed = Column(Float)
    manual = Column(Float)
    passed = Column(Float)
    skip = Column(Float)
    xfailed = Column(Float)
    xpass = Column(Float)
