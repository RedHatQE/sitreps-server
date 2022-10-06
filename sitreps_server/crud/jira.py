from typing import TypeVar

from ..db import Base
from sitreps_server.crud.base import CRUDBase
from sitreps_server.models import Jira
from sitreps_server.schemas import JiraCreate
from sitreps_server.schemas import JiraUpdate

ModelType = TypeVar("ModelType", bound=Base)


class CRUDItem(CRUDBase[Jira, JiraCreate, JiraUpdate]):
    pass


jira = CRUDItem(Jira)
