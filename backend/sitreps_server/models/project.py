from typing import TYPE_CHECKING

from sitreps_server.db import Base
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from .cloc import CLOC  # noqa: F401
    from .code_coverage import CodeCoverage  # noqa: F401
    from .integration_test import IntegrationTest  # noqa: F401
    from .jira import Jira  # noqa: F401
    from .sonarqube import SonarQube  # noqa: F401
    from .unittests import UnitTest  # noqa: F401


class Project(Base):
    """It represent project under ProjectGroup."""

    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)

    group_id = Column(Integer, ForeignKey("groups.id"), index=True)

    cloc = relationship("CLOC", backref="project")
    codecoverage = relationship("CodeCoverage", backref="project")
    integration_test = relationship("IntegrationTest", backref="project")
    jira = relationship("Jira", backref="project")
    sonarqube = relationship("SonarQube", backref="project")
    unittest = relationship("UnitTest", backref="project")
