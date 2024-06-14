"""Unittests crud."""

from typing import TypeVar

from sitreps_server.crud.base import CRUDBase
from sitreps_server.models import UnitTest
from sitreps_server.schemas import UnitTestCreate
from sitreps_server.schemas import UnitTestUpdate

from ..db import Base

ModelType = TypeVar("ModelType", bound=Base)


class CRUDItem(CRUDBase[UnitTest, UnitTestCreate, UnitTestUpdate]):
    pass


unittests = CRUDItem(UnitTest)
