from typing import List
from typing import Optional

from pydantic import BaseModel

from .cloc import CLOCCreate
from .cove_coverage import CodeCoverageCreate
from .integration_test import IntegrationTestCreate
from .jira import JiraCreate
from .project import ProjectCreate
from .project_group import ProjectGroupCreate
from .sonarqube import SonarQubeCreate
from .unittest import UnitTestCreate


class Data(BaseModel):
    project_group: ProjectGroupCreate
    project: ProjectCreate
    jira: Optional[JiraCreate]
    sonarqube: Optional[List[SonarQubeCreate]]
    cloc: Optional[List[CLOCCreate]]
    codecoverage: Optional[List[CodeCoverageCreate]]
    unittests: Optional[List[UnitTestCreate]]
    integrationtests: Optional[List[IntegrationTestCreate]]
