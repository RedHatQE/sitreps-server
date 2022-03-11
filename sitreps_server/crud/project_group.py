from typing import Any
from typing import Optional
from typing import TypeVar

from ..db import Base

ModelType = TypeVar("ModelType", bound=Base)

from sqlalchemy.orm import Session

from sitreps_server.crud.base import CRUDBase
from sitreps_server.models import ProjectGroup
from sitreps_server.schemas.project_group import ProjectGroupCreate, ProjectGroupUpdate


class CRUDItem(CRUDBase[ProjectGroup, ProjectGroupCreate, ProjectGroupUpdate]):
    def get_with_name(self, db: Session, name: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.name == name).first()


project_group = CRUDItem(ProjectGroup)
