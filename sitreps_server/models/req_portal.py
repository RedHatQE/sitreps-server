from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy_json import mutable_json_type

from ..db.types import PortableJSON
from sitreps_server.db import Base


class RequirementsPortalJson(Base):
    """Hold requirements portal avg data in json for all env and plugins."""

    __tablename__ = "req_portal_json"

    time = Column(
        DateTime, default=datetime.utcnow, primary_key=True, index=True
    )  # Just for primary key at we are not going to use it.
    data = Column(mutable_json_type(dbtype=PortableJSON(), nested=True))


# class RequirementsPortal(Base):
#     """Requirements portal historical data."""

#     __tablename__ = "req_portal"

#     time = Column(
#         DateTime, default=datetime.utcnow, primary_key=True, index=True
#     )  # time for time series data.

#     plugin = Column(String)
#     env = Column(String)
#     avg = Column(String)
#     report_time = Column(String)

#     blocked = Column(Float)
#     error  = Column(Float)
#     failed = Column(Float)
#     manual = Column(Float)
#     passed = Column(Float)
#     skip = Column(Float)
#     time = Column(Float)
#     xfailed = Column(Float)
#     xpass = Column(Float)
