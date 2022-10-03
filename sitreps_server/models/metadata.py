from datetime import datetime

from sitreps_server.db import Base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy_json import mutable_json_type
from ..db.types import PortableJSON


class Metadata(Base):
    """Hold test repo related data."""

    __tablename__ = "raw_metadata"

    time = Column(
        DateTime, default=datetime.utcnow, primary_key=True, index=True
    )  # time for time series data.
    repository_id = Column(Integer, ForeignKey("repositories.id"), index=True)

    # Raw Metadata
    meta = Column(mutable_json_type(dbtype=PortableJSON(), nested=True))
