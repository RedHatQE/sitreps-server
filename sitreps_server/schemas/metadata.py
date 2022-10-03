from datetime import datetime
from optparse import Option
from typing import Optional

from pydantic import BaseModel


class MetadataBase(BaseModel):
    time: Optional[datetime]
    
    # repository: instance of Repository for relationship
    repository_id: Optional[int]
    meta: Optional[list]


class MetadataCreate(MetadataBase):
    pass


class Metadata(MetadataBase):
    pass


class MetadataUpdate(MetadataBase):
    pass
