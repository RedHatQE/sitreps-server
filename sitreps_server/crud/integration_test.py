"""Integration tests crud."""

from typing import TypeVar

from sitreps_server.crud.base import CRUDBase
from sitreps_server.models import IntegrationTest
from sitreps_server.schemas import IntegrationTestCreate
from sitreps_server.schemas import IntegrationTestUpdate

from ..db import Base

ModelType = TypeVar("ModelType", bound=Base)


class CRUDItem(CRUDBase[IntegrationTest, IntegrationTestCreate, IntegrationTestUpdate]):
    pass


integration_test = CRUDItem(IntegrationTest)
