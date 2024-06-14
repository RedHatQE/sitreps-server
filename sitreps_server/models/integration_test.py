"""Integration test model."""

from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy_json import mutable_json_type

from sitreps_server.db import Base

from ..db.types import PortableJSON


class IntegrationTest(Base):
    """Hold test repo related data."""

    __tablename__ = "tests"

    time = Column(
        DateTime, default=datetime.utcnow, primary_key=True, index=True
    )  # time for time series data.
    repository_id = Column(Integer, ForeignKey("repositories.id"), index=True)

    total_tests = Column(Integer, index=True)
    customer_scenario = Column(Integer, index=True)
    component = Column(String, index=True)
    # Automation status
    automated = Column(Integer, index=True)
    not_automated = Column(Integer, index=True)
    manual_only = Column(Integer, index=True)
    # Test importance
    critical = Column(Integer, index=True)
    high = Column(Integer, index=True)
    medium = Column(Integer, index=True)
    low = Column(Integer, index=True)
    # Interface
    ui = Column(Integer, index=True)
    non_ui = Column(Integer, index=True)
    # Negative tests
    negative = Column(Integer, index=True)
    # Type
    functional = Column(Integer, index=True)
    non_functional = Column(Integer, index=True)
    # Missing meta
    missing_assignee = Column(Integer, index=True)
    missing_automation_status = Column(Integer, index=True)
    missing_component = Column(Integer, index=True)
    missing_importance = Column(Integer, index=True)
    missing_interface_type = Column(Integer, index=True)
    missing_requirements = Column(Integer, index=True)
    missing_type = Column(Integer, index=True)

    assignees = Column(mutable_json_type(dbtype=PortableJSON()))  # {<name>: <number of tests>, ...}
    requirements = Column(
        mutable_json_type(dbtype=PortableJSON())
    )  # {<requirment>: <number of link tests>, ...}

    meta = Column(mutable_json_type(dbtype=PortableJSON()))

    # Future reserved fields.
    test1 = Column(Integer)
    test2 = Column(Integer)
    test3 = Column(Integer)
