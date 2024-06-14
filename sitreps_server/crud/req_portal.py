"""req-portal crud."""

from typing import TypeVar

from sitreps_server.crud.base import CRUDBase
from sitreps_server.models import RequirementsPortal
from sitreps_server.models import RequirementsPortalJson
from sitreps_server.schemas import RequirementsPortalCreate
from sitreps_server.schemas import RequirementsPortalJsonCreate
from sitreps_server.schemas import RequirementsPortalJsonUpdate
from sitreps_server.schemas import RequirementsPortalUpdate

from ..db import Base

ModelType = TypeVar("ModelType", bound=Base)


class CRUDReqPortal(
    CRUDBase[RequirementsPortal, RequirementsPortalCreate, RequirementsPortalUpdate]
):
    pass


class CRUDReqPortalJson(
    CRUDBase[RequirementsPortalJson, RequirementsPortalJsonCreate, RequirementsPortalJsonUpdate]
):
    pass


req_portal = CRUDReqPortal(RequirementsPortal)
req_portal_json = CRUDReqPortalJson(RequirementsPortalJson)
