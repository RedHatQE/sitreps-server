"""Jira crud."""

from typing import TypeVar

from sitreps_server.crud.base import CRUDBase
from sitreps_server.models import Jira
from sitreps_server.schemas import JiraCreate
from sitreps_server.schemas import JiraUpdate

from ..db import Base

ModelType = TypeVar("ModelType", bound=Base)


class CRUDItem(CRUDBase[Jira, JiraCreate, JiraUpdate]):
    pass


jira = CRUDItem(Jira)
