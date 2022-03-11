from typing import TypeVar

from ..db import Base

ModelType = TypeVar("ModelType", bound=Base)


from sitreps_server.crud.base import CRUDBase
from sitreps_server.models import Jira
from sitreps_server.schemas import JiraCreate, JiraUpdate


class CRUDItem(CRUDBase[Jira, JiraCreate, JiraUpdate]):
    pass


jira = CRUDItem(Jira)
