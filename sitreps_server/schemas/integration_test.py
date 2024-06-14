"""Integration test schema."""

from datetime import datetime

from pydantic import BaseModel


class IntegrationTestBase(BaseModel):
    time: datetime | None

    # repository: instance of Repository for relationship
    repository_id: int | None

    total_tests: int | None
    customer_scenario: int | None
    component: str | None
    # Automatin status
    automated: int | None
    not_automated: int | None
    manual_only: int | None
    # Test importance
    critical: int | None
    high: int | None
    medium: int | None
    low: int | None
    # Interface
    ui: int | None
    non_ui: int | None
    # Negative tests
    negative: int | None
    # Type
    functional: int | None
    non_functional: int | None
    # Missing meta
    missing_assignee: int | None
    missing_automation_status: int | None
    missing_component: int | None
    missing_importance: int | None
    missing_interface_type: int | None
    missing_requirements: int | None
    missing_type: int | None
    assignees: dict | None
    requirements: dict | None  # {<requirment>: <number of link tests>, ...}

    meta: dict | None

    # Future reserved fields.
    test1: int | None
    test2: int | None
    test3: int | None


class IntegrationTestCreate(IntegrationTestBase):
    pass


class IntegrationTest(IntegrationTestBase):
    pass


class IntegrationTestUpdate(IntegrationTestBase):
    pass
