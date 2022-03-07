from typing import List

import crud
import models
import schemas
from database import Base, SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

app = FastAPI()

Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Project Groups APIs


@app.post("/projectgroup", status_code=status.HTTP_201_CREATED, tags=["Project Groups"])
def create_project_group(
    response: Response,
    request: schemas.ProjectGroupCreate,
    db: Session = Depends(get_db),
):
    group = crud.get_project_group_by_name(db=db, name=request.name)
    if group:
        raise HTTPException(
            status_code=status.HTTP_226_IM_USED,
            detail=f"'{request.name}' already available.",
        )
    return crud.create_project_group(db=db, request=request)


@app.get("/projectgroup", status_code=status.HTTP_200_OK, tags=["Project Groups"])
def project_groups(
    response: Response, db: Session = Depends(get_db), offset: int = 0, limit: int = 10
):
    groups = crud.get_project_groups(db=db, offset=offset, limit=limit)

    if not groups:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project Groups not available.",
        )

    return groups


@app.get("/projectgroup/{id}", tags=["Project Groups"])
def project_group(id: int, response: Response, db: Session = Depends(get_db)):
    group = crud.get_project_group(db=db, id=id)

    if not group:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project Group with {id} is not available.",
        )
    return group


@app.get("/projectgroup/{name}", tags=["Project Groups"])
def project_group_by_name(name: str, response: Response, db: Session = Depends(get_db)):
    group = crud.get_project_group_by_name(db=db, name=name)

    if not group:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project Group with '{name}' is not available.",
        )
    return group


# Project APIs


@app.post("/project", status_code=status.HTTP_201_CREATED, tags=["Projects"])
def create_project(
    response: Response, request: schemas.ProjectCreate, db: Session = Depends(get_db)
):
    project = crud.get_project_by_name(db=db, name=request.name)
    if project:
        raise HTTPException(
            status_code=status.HTTP_226_IM_USED,
            detail=f"'{request.name}' already available.",
        )
    return crud.create_project(db=db, request=request)


@app.get("/project", status_code=status.HTTP_200_OK, tags=["Projects"])
def projects(response: Response, db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    project = crud.get_projects(db=db, offset=offset, limit=limit)

    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not available.")

    return project


@app.get("/project/{id}", tags=["Projects"])
def project(id: int, response: Response, db: Session = Depends(get_db)):
    proj = crud.get_project(db=db, id=id)

    if not proj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project with {id} is not available.",
        )
    return proj


@app.get("/project/{name}", tags=["Projects"])
def project_group_by_name(name: str, response: Response, db: Session = Depends(get_db)):
    proj = crud.get_project_by_name(db=db, name=name)

    if not proj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project with '{name}' is not available.",
        )
    return proj


@app.post("/integrationtests", status_code=status.HTTP_201_CREATED, tags=["integrationtest"])
def create_integration_tests(
    response: Response,
    request: schemas.IntegrationTestCreate,
    db: Session = Depends(get_db),
):
    print(request)
    # tests = models.IntegrationTest()
    # crud._add_commit_refresh(db=db, row=tests)


@app.get("/integrationtests", tags=["integrationtest"])
def create_integration_tests(response: Response, db: Session = Depends(get_db)):
    data = db.query(models.IntegrationTest).all()
    # import pdb; pdb.set_trace()
    return data
    # y = {i: x.data for i, x in enumerate(data)}
    # json_compatible_item_data = jsonable_encoder(y)
    # return JSONResponse(content=json_compatible_item_data)


@app.post("/data", status_code=status.HTTP_201_CREATED)
def dump_data(request: schemas.Data, db: Session = Depends(get_db)):
    data = request.data
    try:
        proj_data = data["project"]
        project = crud.get_project_by_name(db=db, name=proj_data["name"])

        if not project:
            new_project = models.Project(**proj_data)
            crud._add_commit_refresh(db=db, row=new_project)
            print(f"{proj_data['name']} created.")

        jira_data = data["jira"]
        if jira_data:
            new_jira = models.Jira(**jira_data)
            crud._add_commit_refresh(db=db, row=new_jira)

        for sonar_data in data["sonarqube"]:
            if "vulnerabilities" in sonar_data:
                # only if sonar data available.
                sonar = models.SonarQube(**sonar_data)
                crud._add_commit_refresh(db=db, row=sonar)

        for unittest_data in data["unittests"]:
            unittest = models.UnitTest(**unittest_data)
            crud._add_commit_refresh(db=db, row=unittest)

        for cloc_data in data["cloc"]:
            cloc = models.CLOC(**cloc_data)
            crud._add_commit_refresh(db=db, row=cloc)

        for codecov_data in data["codecoverage"]:
            cov = models.CodeCoverage(**codecov_data)
            crud._add_commit_refresh(db=db, row=cov)
        for test_data in data["integrationtests"].values():
            tests = models.IntegrationTest(**test_data)
            crud._add_commit_refresh(db=db, row=tests)

    except Exception as e:
        db.rollback()
        print(e)


@app.get("/data")
def get_data(db: Session = Depends(get_db)):
    proj = crud.get_projects(db=db)
    json_compatible_item_data = jsonable_encoder(proj)
    return JSONResponse(content=json_compatible_item_data)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("sitreps:app", reload=True, access_log=True)
