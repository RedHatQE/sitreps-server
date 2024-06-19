"""Bulk operation schema."""

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
    repository: RepositoryCreate | None = None
    integrationtests: IntegrationTestCreate | None = None
    metadata: MetadataCreate | None = None
    sonarqube: SonarQubeCreate | None = None
    cloc: CLOCCreate | None = None
    codecoverage: CodeCoverageCreate | None = None
    unittests: UnitTestCreate | None = None


class Data(BaseModel):
    project_group: ProjectGroupCreate
    project: ProjectCreate
    repos: list[RepoData]
    jira: JiraCreate | None = None
