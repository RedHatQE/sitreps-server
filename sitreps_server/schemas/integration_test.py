"""Integration test schema."""

from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class IntegrationTestBase(BaseModel):
    time: datetime | None = None

    # repository: instance of Repository for relationship
    repository_id: int | None = None

    total_tests: int | None = None
    customer_scenario: int | None = None
    component: str | None = None
    # Automatin status
    automated: int | None = None
    not_automated: int | None = None
    manual_only: int | None = None
    # Test importance
    critical: int | None = None
    high: int | None = None
    medium: int | None = None
    low: int | None = None
    # Interface
    ui: int | None = None
    non_ui: int | None = None
    # Negative tests
    negative: int | None = None
    # Type
    functional: int | None = None
    non_functional: int | None = None
    # Missing meta
    missing_assignee: int | None = None
    missing_automation_status: int | None = None
    missing_component: int | None = None
    missing_importance: int | None = None
    missing_interface_type: int | None = None
    missing_requirements: int | None = None
    missing_type: int | None = None
    assignees: dict | None = None
    requirements: dict | None = None  # {<requirment>: <number of link tests>, ...}

    meta: dict | None = None

    # Future reserved fields.
    test1: int | None = None
    test2: int | None = None
    test3: int | None = None


class IntegrationTestCreate(IntegrationTestBase):
    model_config = ConfigDict(from_attributes=True)


class IntegrationTest(IntegrationTestBase):
    pass


class IntegrationTestUpdate(IntegrationTestBase):
    pass
