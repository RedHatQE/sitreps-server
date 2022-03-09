from typing import Any

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from sitreps_server import schemas
from sqlalchemy.orm import Session

from .deps import get_db

router = APIRouter()


@router.get("/")
def get_status() -> Any:
    """Server status"""
    return {"details": "ok"}


@router.post("/", status_code=status.HTTP_201_CREATED)
def dump_data(request: schemas.Data, db: Session = Depends(get_db)):
    return {"details": "Not implemented."}
    # data = request.data
    # try:
    #     proj_data = data["project"]
    #     project = crud.get_project_by_name(db=db, name=proj_data["name"])
    #
    #     if not project:
    #         new_project = models.Project(**proj_data)
    #         crud._add_commit_refresh(db=db, row=new_project)
    #         print(f"{proj_data['name']} created.")
    #
    #     jira_data = data["jira"]
    #     if jira_data:
    #         new_jira = models.Jira(**jira_data)
    #         crud._add_commit_refresh(db=db, row=new_jira)
    #
    #     for sonar_data in data["sonarqube"]:
    #         if "vulnerabilities" in sonar_data:
    #             # only if sonar data available.
    #             sonar = models.SonarQube(**sonar_data)
    #             crud._add_commit_refresh(db=db, row=sonar)
    #
    #     for unittest_data in data["unittests"]:
    #         unittest = models.UnitTest(**unittest_data)
    #         crud._add_commit_refresh(db=db, row=unittest)
    #
    #     for cloc_data in data["cloc"]:
    #         cloc = models.CLOC(**cloc_data)
    #         crud._add_commit_refresh(db=db, row=cloc)
    #
    #     for codecov_data in data["codecoverage"]:
    #         cov = models.CodeCoverage(**codecov_data)
    #         crud._add_commit_refresh(db=db, row=cov)
    #     for test_data in data["integrationtests"].values():
    #         tests = models.IntegrationTest(**test_data)
    #         crud._add_commit_refresh(db=db, row=tests)
    #
    # except Exception as e:
    #     db.rollback()
    #     print(e)
