from typing import TypeVar

from ..db import Base

ModelType = TypeVar("ModelType", bound=Base)


from sitreps_server.crud.base import CRUDBase
from sitreps_server.models import SonarQube
from sitreps_server.schemas import SonarQubeCreate, SonarQubeUpdate


class CRUDItem(CRUDBase[SonarQube, SonarQubeCreate, SonarQubeUpdate]):
    pass


sonarqube = CRUDItem(SonarQube)
