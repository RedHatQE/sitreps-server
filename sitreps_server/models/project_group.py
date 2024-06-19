"""Project group model."""

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from sitreps_server.db import Base


class ProjectGroup(Base):
    """Project group table hold data of org/project having multiple projects."""

    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    projects = relationship("Project", backref="group")
