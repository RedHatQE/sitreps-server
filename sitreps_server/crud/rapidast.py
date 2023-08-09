from typing import TypeVar

from ..db import Base
from sitreps_server.crud.base import CRUDBase
from sitreps_server.models import Rapidast
from sitreps_server.models import RapidastReport
from sitreps_server.schemas import RapidastCreate
from sitreps_server.schemas import RapidastReportCreate
from sitreps_server.schemas import RapidastReportUpdate
from sitreps_server.schemas import RapidastUpdate


ModelType = TypeVar("ModelType", bound=Base)


class CRUDRapidast(CRUDBase[Rapidast, RapidastCreate, RapidastUpdate]):
    pass


class CRUDRapidastReport(CRUDBase[RapidastReport, RapidastReportCreate, RapidastReportUpdate]):
    pass


rapidast_report = CRUDRapidastReport(RapidastReport)
rapidast = CRUDRapidast(Rapidast)
