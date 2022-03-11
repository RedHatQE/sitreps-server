from datetime import datetime

from sitreps_server.db import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.dialects.postgresql import JSON


class IntegrationTest(Base):
    """Hold test repo related data."""

    __tablename__ = "tests"

    time = Column(
        DateTime, default=datetime.utcnow, primary_key=True, index=True
    )  # time for time series data.
    project_id = Column(Integer, ForeignKey("projects.id"), index=True)
    unique = Column(Boolean, index=True)

    all = Column(Integer, index=True)  # automated + manual
    automated = Column(Integer, index=True)
    manual = Column(Integer, index=True)

    ui = Column(Integer, index=True)
    non_ui = Column(Integer, index=True)

    automated_ui = Column(Integer, index=True)
    automated_non_ui = Column(Integer, index=True)
    automated_other = Column(Integer, index=True)  # automated - automated_ui - automated_non_ui

    manual_ui = Column(Integer, index=True)
    manual_non_ui = Column(Integer, index=True)
    manual_other = Column(Integer, index=True)

    # Test importance
    critical = Column(Integer, index=True)
    high = Column(Integer, index=True)
    medium = Column(Integer, index=True)
    low = Column(Integer, index=True)

    # Missing metadata (like test missing assignee)
    missing_interfacetype = Column(Integer, index=True)
    missing_assignee = Column(Integer, index=True)
    missing_caseimportance = Column(Integer, index=True)
    missing_casecomponent = Column(Integer, index=True)
    missing_requirements = Column(Integer, index=True)

    assignees = Column(JSON)  # {<name>: <number of tests>, ...}
    requirements = Column(JSON)  # {<requirment>: <number of link tests>, ...}
    components = Column(JSON)
