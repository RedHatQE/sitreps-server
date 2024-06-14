"""Sonarqube schema."""

from datetime import datetime

from pydantic import BaseModel


class SonarQubeBase(BaseModel):
    time: datetime | None

    # repository: instance of Repository for relationship
    repository_id: int | None

    project: str | None
    vulnerabilities: int
    code_smells: int
    security_hotspots: int
    bugs: int

    meta: dict | None


class SonarQube(SonarQubeBase):
    pass


class SonarQubeCreate(SonarQubeBase):
    pass


class SonarQubeUpdate(SonarQubeBase):
    pass
