"""Project crud."""

from typing import Any
from typing import TypeVar

from sqlalchemy.orm import Session

from sitreps_server.crud.base import CRUDBase
from sitreps_server.models import Project
from sitreps_server.schemas import ProjectCreate
from sitreps_server.schemas import ProjectUpdate

from ..db import Base

ModelType = TypeVar("ModelType", bound=Base)


class CRUDItem(CRUDBase[Project, ProjectCreate, ProjectUpdate]):
    def get_with_name(self, db: Session, name: Any) -> ModelType | None:
        """Get item with name."""
        return db.query(self.model).filter(self.model.name == name).first()


project = CRUDItem(Project)
