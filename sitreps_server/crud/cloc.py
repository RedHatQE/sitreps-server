"""CLOC crud."""

from typing import TypeVar

from sitreps_server.crud.base import CRUDBase
from sitreps_server.models import CLOC
from sitreps_server.schemas import CLOCCreate
from sitreps_server.schemas import CLOCUpdate

from ..db import Base

ModelType = TypeVar("ModelType", bound=Base)


class CRUDItem(CRUDBase[CLOC, CLOCCreate, CLOCUpdate]):
    pass


cloc = CRUDItem(CLOC)
