"""Unit-tests model."""

from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from sitreps_server.db import Base


class UnitTestResult(Base):
    """UnitTestResults table to store test results for different CI tools."""

    __tablename__ = "unittest_results"

    # Unique ID for each test result
    id = Column(
        Integer, primary_key=True, autoincrement=True
    )  # Auto-incrementing unique identifier for each row

    # Time of the test run
    time = Column(DateTime, default=datetime.utcnow, index=True)

    # Foreign Key linking to repositories table
    repository_id = Column(Integer, ForeignKey("repositories.id"), index=True)

    # CI tool name (e.g., 'gh_action', 'travis', etc.)
    ci_link = Column(String, default=None)
    ci_name = Column(String, index=True)

    # Framework name, such as 'jest', 'cypress', etc.
    framework_name = Column(String, index=True)

    # Test counts for the framework
    passed = Column(Integer, default=0)
    failed = Column(Integer, default=0)
    skipped = Column(Integer, default=0)
    total = Column(Integer, default=0)
