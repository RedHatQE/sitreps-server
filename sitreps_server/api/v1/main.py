from typing import Any

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from sqlalchemy.orm import Session

from .deps import get_db
from sitreps_server import crud
from sitreps_server import schemas

router = APIRouter()


@router.get("/", include_in_schema=False)
async def get_status() -> Any:
    """Server status"""
    return {"details": "ok"}


@router.post("/", status_code=status.HTTP_201_CREATED)
async def dump_data(data: schemas.Data, db: Session = Depends(get_db)):
    try:
        # project group
        pg_schema = data.project_group
        pg = crud.project_group.get_with_name(db, name=pg_schema.name)
        if pg:
            print(f"\nProject group {pg.name} alredy exists.")
        else:
            pg = crud.project_group.create(db=db, obj_in=pg_schema)
            print(f"\nProject Group {pg.name} created.")

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

        for repo_data in data.repos:
            # repository
            repo_schema = repo_data.repository
            repo = crud.repository.get_with_name(db, name=repo_schema.name)
            if repo:
                print(f"\nRepository {repo.name} already exists.")
            else:
                repo_schema.project_id = proj.id
                repo = crud.repository.create(db=db, obj_in=repo_schema)
                print(f"\nRepository {repo.name} creted.")

            # Integration tests
            test_schema = repo_data.integrationtests
            if test_schema:
                test_schema.repository_id = repo.id
                tests_row = crud.integration_test.create(db=db, obj_in=test_schema)
                print(f"{tests_row.time}: New Integration Test entry")
            else:
                print("Skipping Integration Test as data not found.")

            # Metadata of integration test
            metadata_schema = repo_data.metadata
            if metadata_schema:
                metadata_schema.repository_id = repo.id
                meta_row = crud.metadata.create(db=db, obj_in=metadata_schema)
                print(f"{meta_row.time}: New metadata entry")
            else:
                print("Skipping metadata as data not found.")

            # CLOC
            cloc_schema = repo_data.cloc
            if cloc_schema:
                cloc_schema.repository_id = repo.id
                cloc_row = crud.cloc.create(db=db, obj_in=cloc_schema)
                print(f"{cloc_row.time}: New CLOC entry")
            else:
                print("Skipping CLOC as data not found.")

            # Code Coverage
            codecoverage_schema = repo_data.codecoverage
            if codecoverage_schema:
                codecoverage_schema.repository_id = repo.id
                cov_row = crud.code_coverage.create(db=db, obj_in=codecoverage_schema)
                print(f"{cov_row.time}: New code coverage entry")
            else:
                print("Skipping code coverage as data not found.")

            # sonarqube
            sonarqube_schema = repo_data.sonarqube
            if sonarqube_schema:
                sonarqube_schema.repository_id = repo.id
                sonar_row = crud.sonarqube.create(db=db, obj_in=sonarqube_schema)
                print(f"{sonar_row.time}: New sonarqube entry")
            else:
                print("Skipping sonarqube as data not found.")

            # Unit tests
            unittests_schema = repo_data.unittests
            if unittests_schema:
                unittests_schema.repository_id = repo.id
                unittests_row = crud.unittests.create(db=db, obj_in=unittests_schema)
                print(f"{unittests_row.time}: New Unit Tests entry")
            else:
                print("Skipping Unit Tests as data not found.")

    except Exception as e:
        db.rollback()
        print(e)
