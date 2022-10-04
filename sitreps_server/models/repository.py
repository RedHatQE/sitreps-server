from operator import index
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
    from .sonarqube import SonarQube  # noqa: F401
    from .unittests import UnitTest  # noqa: F401


class Repository(Base):
    """It represent Repository under Project."""

    __tablename__ = "repositories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    title = Column(String, index=True)
    type = Column(String, index=True)
    url = Column(String, index=True)

    project_id = Column(Integer, ForeignKey("projects.id"), index=True)

    cloc = relationship("CLOC", backref="repository")
    codecoverage = relationship("CodeCoverage", backref="repository")
    integration_test = relationship("IntegrationTest", backref="repository")
    sonarqube = relationship("SonarQube", backref="repository")
    unittest = relationship("UnitTest", backref="repository")