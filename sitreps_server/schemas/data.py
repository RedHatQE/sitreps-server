from typing import List
from typing import Optional

from pydantic import BaseModel

from .cloc import CLOCCreate
from .cove_coverage import CodeCoverageCreate
from .integration_test import IntegrationTestCreate
from .jira import JiraCreate
from .metadata import MetadataCreate
from .project import ProjectCreate
from .project_group import ProjectGroupCreate
from .repository import RepositoryCreate
from .sonarqube import SonarQubeCreate
from .unittest import UnitTestCreate


class RepoData(BaseModel):
    repository: Optional[RepositoryCreate]
    integrationtests: Optional[IntegrationTestCreate]
    metadata: Optional[MetadataCreate]
    sonarqube: Optional[SonarQubeCreate]
    cloc: Optional[CLOCCreate]
    codecoverage: Optional[CodeCoverageCreate]
    unittests: Optional[UnitTestCreate]


class Data(BaseModel):
    project_group: ProjectGroupCreate
    project: ProjectCreate
    repos: List[RepoData]
    jira: Optional[JiraCreate]
