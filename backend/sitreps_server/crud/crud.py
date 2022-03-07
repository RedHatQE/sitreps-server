import models
import schemas
from sqlalchemy.orm import Session


def _add_commit_refresh(db, row):
    db.add(row)
    db.commit()
    db.refresh(row)


def create_project_group(db: Session, request: schemas.ProjectGroupCreate):
    new_group = models.ProjectGroup(
        name=request.name, title=request.title, description=request.description
    )
    db.add(new_group)
    db.commit()
    db.refresh(new_group)
    return new_group


def get_project_groups(db: Session, offset: int = 0, limit: int = 10):
    return db.query(models.ProjectGroup).offset(offset).limit(limit).all()


def get_project_group(db: Session, id: int):
    return db.query(models.ProjectGroup).filter(models.ProjectGroup.id == id).first()


def get_project_group_by_name(db: Session, name: str):
    return db.query(models.ProjectGroup).filter(models.ProjectGroup.name == name).first()


def create_project(db: Session, request: schemas.Project):
    project = models.Project(
        name=request.name,
        title=request.title,
        description=request.description,
        group_id=request.group_id,
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def get_projects(db: Session, offset: int = 0, limit: int = 10):
    return db.query(models.Project).offset(offset).limit(limit).all()


def get_project(db: Session, id: int):
    return db.query(models.Project).filter(models.Project.id == id).first()


def get_project_by_name(db: Session, name: str):
    return db.query(models.Project).filter(models.Project.name == name).first()


def create_project(db: Session, request: schemas.Project):
    project = models.Project(
        name=request.name,
        title=request.title,
        description=request.description,
        group_id=request.group_id,
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def get_projects(db: Session, offset: int = 0, limit: int = 10):
    return db.query(models.Project).offset(offset).limit(limit).all()


def get_project(db: Session, id: int):
    return db.query(models.Project).filter(models.Project.id == id).first()


def get_project_by_name(db: Session, name: str):
    return db.query(models.Project).filter(models.Project.name == name).first()


def create_project(db: Session, request: schemas.Project):
    project = models.Project(
        name=request.name,
        title=request.title,
        description=request.description,
        group_id=request.group_id,
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def get_projects(db: Session, offset: int = 0, limit: int = 10):
    return db.query(models.Project).offset(offset).limit(limit).all()


def get_project(db: Session, id: int):
    return db.query(models.Project).filter(models.Project.id == id).first()


def get_project_by_name(db: Session, name: str):
    return db.query(models.Project).filter(models.Project.name == name).first()
