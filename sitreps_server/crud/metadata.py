"""Metadata crud."""

from typing import TypeVar

from sitreps_server.crud.base import CRUDBase
from sitreps_server.models import Metadata
from sitreps_server.schemas import MetadataCreate
from sitreps_server.schemas import MetadataUpdate

from ..db import Base

ModelType = TypeVar("ModelType", bound=Base)


class CRUDItem(CRUDBase[Metadata, MetadataCreate, MetadataUpdate]):
    pass


metadata = CRUDItem(Metadata)
