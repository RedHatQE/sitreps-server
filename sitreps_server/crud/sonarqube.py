from typing import TypeVar

from ..db import Base
from sitreps_server.crud.base import CRUDBase
from sitreps_server.models import SonarQube
from sitreps_server.schemas import SonarQubeCreate
from sitreps_server.schemas import SonarQubeUpdate

ModelType = TypeVar("ModelType", bound=Base)


class CRUDItem(CRUDBase[SonarQube, SonarQubeCreate, SonarQubeUpdate]):
    pass


sonarqube = CRUDItem(SonarQube)
