from typing import TypeVar

from ..db import Base
from sitreps_server.crud.base import CRUDBase
from sitreps_server.models import IntegrationTest
from sitreps_server.schemas import IntegrationTestCreate
from sitreps_server.schemas import IntegrationTestUpdate

ModelType = TypeVar("ModelType", bound=Base)


class CRUDItem(CRUDBase[IntegrationTest, IntegrationTestCreate, IntegrationTestUpdate]):
    pass


integration_test = CRUDItem(IntegrationTest)
