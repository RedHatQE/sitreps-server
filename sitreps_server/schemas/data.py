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
    repository: RepositoryCreate | None
    integrationtests: IntegrationTestCreate | None
    metadata: MetadataCreate | None
    sonarqube: SonarQubeCreate | None
    cloc: CLOCCreate | None
    codecoverage: CodeCoverageCreate | None
    unittests: UnitTestCreate | None


class Data(BaseModel):
    project_group: ProjectGroupCreate
    project: ProjectCreate
    repos: list[RepoData]
    jira: JiraCreate | None
