from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class IntegrationTestBase(BaseModel):
    time: Optional[datetime]
    
    # repository: instance of Repository for relationship
    repository_id: Optional[int]

    total_tests: Optional[int]
    customer_scenario: Optional[int]
    component: Optional[str]
    # Automatin status
    automated: Optional[int]
    not_automated: Optional[int]
    manual_only: Optional[int]
    # Test importance
    critical: Optional[int]
    high: Optional[int]
    medium: Optional[int]
    low: Optional[int]
    # Interface
    ui: Optional[int]
    non_ui: Optional[int]
    # Negative tests
    negative: Optional[int]
    # Type
    functional: Optional[int]
    non_functional: Optional[int]
    # Missing meta
    missing_assignee: Optional[int]
    missing_automation_status: Optional[int]
    missing_component: Optional[int]
    missing_importance: Optional[int]
    missing_interface_type: Optional[int]
    missing_requirements: Optional[int]
    missing_type: Optional[int]
    assignees: Optional[dict]
    requirements: Optional[dict]  # {<requirment>: <number of link tests>, ...}

    meta: Optional[dict]

    # Future reserved fields.
    test1: Optional[int]
    test2: Optional[int]
    test3: Optional[int]


class IntegrationTestCreate(IntegrationTestBase):
    pass


class IntegrationTest(IntegrationTestBase):
    pass


class IntegrationTestUpdate(IntegrationTestBase):
    pass
