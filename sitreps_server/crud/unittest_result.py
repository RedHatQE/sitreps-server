"""Unittests crud."""

from typing import TypeVar

from sitreps_server.crud.base import CRUDBase
from sitreps_server.models import UnitTestResult
from sitreps_server.schemas import UnitTestResultCreate
from sitreps_server.schemas import UnitTestResultUpdate

from ..db import Base

ModelType = TypeVar("ModelType", bound=Base)


class CRUDItem(CRUDBase[UnitTestResult, UnitTestResultCreate, UnitTestResultUpdate]):
    pass


unittest_result = CRUDItem(UnitTestResult)
