from typing import TypeVar

from ..db import Base
from sitreps_server.crud.base import CRUDBase
from sitreps_server.models import UnitTest
from sitreps_server.schemas import UnitTestCreate
from sitreps_server.schemas import UnitTestUpdate

ModelType = TypeVar("ModelType", bound=Base)


class CRUDItem(CRUDBase[UnitTest, UnitTestCreate, UnitTestUpdate]):
    pass


unittests = CRUDItem(UnitTest)
