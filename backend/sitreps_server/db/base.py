from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from ..core.config import settings


def get_db_url():
    if settings.DATABASE_URL:
        return settings.DATABASE_URL
    user = settings.POSTGRESQL_USER
    password = settings.POSTGRESQL_PASSWORD
    server = settings.POSTGRESQL_SERVER
    db = settings.POSTGRESQL_DATABASE
    return f"postgresql://{user}:{password}@{server}/{db}"


SQLALCHEMY_DATABASE_URL = get_db_url()

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
