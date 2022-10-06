from datetime import datetime

from sitreps_server.db import Base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy_json import mutable_json_type
from ..db.types import PortableJSON


class CLOC(Base):
    """Count Line of Code."""

    __tablename__ = "cloc"

    time = Column(
        DateTime, default=datetime.utcnow, primary_key=True, index=True
    )  # time for time series data.
    cloc = Column(Integer, index=True)
    meta = Column(mutable_json_type(dbtype=PortableJSON()))

    repository_id = Column(Integer, ForeignKey("repositories.id"), index=True)
