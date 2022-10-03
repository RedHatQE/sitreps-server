from typing import Any
from typing import Optional
from typing import TypeVar

from ..db import Base

ModelType = TypeVar("ModelType", bound=Base)

from sqlalchemy.orm import Session

from sitreps_server.crud.base import CRUDBase
from sitreps_server.models import Repository
from sitreps_server.schemas import RepositoryCreate, RepositoryUpdate


class CRUDItem(CRUDBase[Repository, RepositoryCreate, RepositoryUpdate]):
    def get_with_name(self, db: Session, name: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.name == name).first()


repository = CRUDItem(Repository)
