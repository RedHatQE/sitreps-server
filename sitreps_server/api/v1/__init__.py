from fastapi import APIRouter

from .cloc import router as cloc_router
from .code_coverage import router as cov_router
from .integration_test import router as test_router
from .jira import router as jira_router
from .main import router as main_router
from .metadata import router as metadata_router
from .project import router as proj_router
from .project_groups import router as pg_router
from .rapidast import router as rapidast_router
from .repository import router as repo_router
from .req_portal import router as req_portal_router
from .sonarqube import router as sonar_router
from .unittests import router as unittest_router

api_router = APIRouter()
api_router.include_router(main_router)  # default
api_router.include_router(pg_router, prefix="/projectgroups", tags=["Project Groups"])
api_router.include_router(proj_router, prefix="/projects", tags=["Projects"])
api_router.include_router(jira_router, prefix="/jira", tags=["Jira"])
api_router.include_router(repo_router, prefix="/repositories", tags=["Repositories"])
api_router.include_router(cloc_router, prefix="/cloc", tags=["Count Line of Code"])
api_router.include_router(cov_router, prefix="/coverage", tags=["Code Coverage"])
api_router.include_router(test_router, prefix="/integrationtest", tags=["Integration Tests"])
api_router.include_router(metadata_router, prefix="/metadata", tags=["Metadata"])
api_router.include_router(sonar_router, prefix="/sonarqube", tags=["SonarQube"])
api_router.include_router(unittest_router, prefix="/unittests", tags=["Unit Tests"])
api_router.include_router(req_portal_router, prefix="/req-portal", tags=["Requirements Portal"])
api_router.include_router(rapidast_router, prefix="/rapidast", tags=["RapiDAST"])
