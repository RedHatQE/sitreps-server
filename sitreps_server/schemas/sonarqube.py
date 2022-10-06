from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SonarQubeBase(BaseModel):
    time: Optional[datetime]

    # repository: instance of Repository for relationship
    repository_id: Optional[int]

    project: Optional[str]
    vulnerabilities: int
    code_smells: int
    security_hotspots: int
    bugs: int

    meta: Optional[dict]


class SonarQube(SonarQubeBase):
    pass


class SonarQubeCreate(SonarQubeBase):
    pass


class SonarQubeUpdate(SonarQubeBase):
    pass
