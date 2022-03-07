from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SonarQubeBase(BaseModel):
    time: Optional[datetime]
    repo_name: Optional[str]  # If multiple repos like backend/frontend
    vulnerabilities: int
    code_smells: int
    security_hotspots: int
    bugs: int
    # project: instance of Project for relationship
    project_id: Optional[int]


class SonarQube(SonarQubeBase):
    pass


class SonarQubeCreate(SonarQubeBase):
    pass
