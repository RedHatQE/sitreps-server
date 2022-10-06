from typing import Any
from typing import Optional
from typing import TypeVar

from sqlalchemy.orm import Session

from ..db import Base
from sitreps_server.crud.base import CRUDBase
from sitreps_server.models import ProjectGroup
from sitreps_server.schemas.project_group import ProjectGroupCreate
from sitreps_server.schemas.project_group import ProjectGroupUpdate

ModelType = TypeVar("ModelType", bound=Base)


class CRUDItem(CRUDBase[ProjectGroup, ProjectGroupCreate, ProjectGroupUpdate]):
    def get_with_name(self, db: Session, name: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.name == name).first()


project_group = CRUDItem(ProjectGroup)
