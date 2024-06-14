"""Metadata schema."""

from datetime import datetime

from pydantic import BaseModel


class MetadataBase(BaseModel):
    time: datetime | None

    # repository: instance of Repository for relationship
    repository_id: int | None
    meta: list | None


class MetadataCreate(MetadataBase):
    pass


class Metadata(MetadataBase):
    pass


class MetadataUpdate(MetadataBase):
    pass
