from typing import TypeVar

from ..db import Base
from sitreps_server.crud.base import CRUDBase
from sitreps_server.models import Metadata
from sitreps_server.schemas import MetadataCreate
from sitreps_server.schemas import MetadataUpdate

ModelType = TypeVar("ModelType", bound=Base)


class CRUDItem(CRUDBase[Metadata, MetadataCreate, MetadataUpdate]):
    pass


metadata = CRUDItem(Metadata)
