"""Sonarqube schema."""

from datetime import datetime

from pydantic import BaseModel


class SonarQubeBase(BaseModel):
    time: datetime | None = None

    # repository: instance of Repository for relationship
    repository_id: int | None = None

    vulnerabilities: int
    code_smells: int
    security_hotspots: int
    bugs: int
    sonar_last_analysis: datetime | None = None
    meta: dict | None = None


class SonarQube(SonarQubeBase):
    pass


class SonarQubeCreate(SonarQubeBase):
    pass


class SonarQubeUpdate(SonarQubeBase):
    pass
