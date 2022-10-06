from typing import TypeVar

from ..db import Base
from sitreps_server.crud.base import CRUDBase
from sitreps_server.models import CLOC
from sitreps_server.schemas import CLOCCreate
from sitreps_server.schemas import CLOCUpdate

ModelType = TypeVar("ModelType", bound=Base)


class CRUDItem(CRUDBase[CLOC, CLOCCreate, CLOCUpdate]):
    pass


cloc = CRUDItem(CLOC)
