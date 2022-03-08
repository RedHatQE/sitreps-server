from typing import TypeVar

from ..db import Base

ModelType = TypeVar("ModelType", bound=Base)


from sitreps_server.crud.base import CRUDBase
from sitreps_server.models import CodeCoverage
from sitreps_server.schemas import CodeCoverageCreate, CodeCoverageUpdate


class CRUDItem(CRUDBase[CodeCoverage, CodeCoverageCreate, CodeCoverageUpdate]):
    pass


code_coverage = CRUDItem(CodeCoverage)
