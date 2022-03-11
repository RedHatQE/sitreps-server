from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class IntegrationTestBase(BaseModel):
    time: Optional[datetime]
    project_id: Optional[int]
    unique: bool

    all: Optional[int]
    automated: Optional[int]
    manual: Optional[int]

    ui: Optional[int]
    non_ui: Optional[int]

    automated_ui: Optional[int]
    automated_non_ui: Optional[int]
    automated_other: Optional[int]  # automated - automated_ui - automated_non_ui

    manual_ui: Optional[int]
    manual_non_ui: Optional[int]
    manual_other: Optional[int]

    # Test importance
    critical: Optional[int]
    high: Optional[int]
    medium: Optional[int]
    low: Optional[int]

    # Missing metadata (like test missing assignee)
    missing_interfacetype: Optional[int]
    missing_assignee: Optional[int]
    missing_caseimportance: Optional[int]
    missing_casecomponent: Optional[int]
    missing_requirements: Optional[int]

    assignees: Optional[dict]  # {<name>: <number of tests>, ...}
    requirements: Optional[dict]  # {<requirment>: <number of link tests>, ...}
    components: Optional[dict]


class IntegrationTestCreate(IntegrationTestBase):
    pass


class IntegrationTest(IntegrationTestBase):
    pass


class IntegrationTestUpdate(IntegrationTestBase):
    pass
