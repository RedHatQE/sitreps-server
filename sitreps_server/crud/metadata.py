from typing import TypeVar

from ..db import Base

ModelType = TypeVar("ModelType", bound=Base)


from sitreps_server.crud.base import CRUDBase
from sitreps_server.models import Metadata
from sitreps_server.schemas import MetadataCreate, MetadataUpdate


class CRUDItem(CRUDBase[Metadata, MetadataCreate, MetadataUpdate]):
    pass


metadata = CRUDItem(Metadata)
