"""Sonarqube crud."""

from typing import TypeVar

from sitreps_server.crud.base import CRUDBase
from sitreps_server.models import SonarQube
from sitreps_server.schemas import SonarQubeCreate
from sitreps_server.schemas import SonarQubeUpdate

from ..db import Base

ModelType = TypeVar("ModelType", bound=Base)


class CRUDItem(CRUDBase[SonarQube, SonarQubeCreate, SonarQubeUpdate]):
    pass


sonarqube = CRUDItem(SonarQube)
