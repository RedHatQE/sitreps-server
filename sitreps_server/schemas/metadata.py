"""Metadata schema."""

from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class MetadataBase(BaseModel):
    time: datetime | None = None

    # repository: instance of Repository for relationship
    repository_id: int | None = None
    meta: list | None = None


class MetadataCreate(MetadataBase):
    model_config = ConfigDict(from_attributes=True)


class Metadata(MetadataBase):
    pass


class MetadataUpdate(MetadataBase):
    pass
