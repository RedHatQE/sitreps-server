from typing import Any

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sitreps_server import crud
from sitreps_server import schemas
from sqlalchemy.orm import Session

from .deps import get_db

router = APIRouter()


@router.get("/")
def get_status() -> Any:
    """Server status"""
    return {"details": "ok"}


@router.post("/", status_code=status.HTTP_201_CREATED)
def dump_data(data: schemas.Data, db: Session = Depends(get_db)):
    try:
        # project group
        pg_schema = data.project_group
        pg = crud.project_group.get_with_name(db, name=pg_schema.name)
        if not pg:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"'{pg_schema.name}' not found. Please contact to admin.",
            )
        print(f"Project group {pg.name} found.")

        # project
        project_schema = data.project
        proj = crud.project.get_with_name(db, name=project_schema.name)
        if proj:
            print(f"Project {proj.name} already exists.")
        else:
            project_schema.group_id = pg.id
            proj = crud.project.create(db=db, obj_in=project_schema)
            print(f"Project {proj.name} created.")

        # jira
        if data.jira:
            data.jira.project_id = proj.id
            jira = crud.jira.create(db=db, obj_in=data.jira)
            print(f"New jira entry: {jira.time}")
        else:
            print("Skipping jira as data not found.")

        # sonarqube
        if data.sonarqube:
            for sonar in data.sonarqube:
                sonar.project_id = proj.id
                sonar_row = crud.sonarqube.create(db=db, obj_in=sonar)
                print(f"New sonar entry: {sonar_row.time} > {sonar_row.repo_name}")
        else:
            print("Skipping sonarqube as data not found.")

        # CLOC
        if data.cloc:
            for cloc in data.cloc:
                cloc.project_id = proj.id
                cloc_row = crud.cloc.create(db=db, obj_in=cloc)
                print(f"New CLOC entry: {cloc_row.time} > {cloc_row.repo_name}")
        else:
            print("Skipping CLOC as data not found.")

        # Code Coverage
        if data.codecoverage:
            for codecoverage in data.codecoverage:
                codecoverage.project_id = proj.id
                cov_row = crud.code_coverage.create(db=db, obj_in=codecoverage)
                print(f"New code coverage entry: {cov_row.time} > {cov_row.repo_name}")
        else:
            print("Skipping code coverage as data not found.")

        # Unit tests
        if data.unittests:
            for unittests in data.unittests:
                unittests.project_id = proj.id
                unittests_row = crud.unittests.create(db=db, obj_in=unittests)
                print(f"New Unit Tests entry: {unittests_row.time} > {unittests_row.repo_name}")
        else:
            print("Skipping Unit Tests as data not found.")

        # Unit tests
        if data.integrationtests:
            for test in data.integrationtests:
                test.project_id = proj.id
                tests_row = crud.integration_test.create(db=db, obj_in=test)
                print(f"New Unit Tests entry: {tests_row.time} > {tests_row.unique}")
        else:
            print("Skipping Unit Tests as data not found.")

    except Exception as e:
        db.rollback()
        print(e)
