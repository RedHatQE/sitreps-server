# flake8: noqa
import os
import sys
from logging.config import fileConfig
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context


# This allows relative import to work correctly
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from sitreps_server.db import Base
from sitreps_server.models import (
    CLOC,
    CodeCoverage,
    IntegrationTest,
    Jira,
    Metadata,
    Project,
    ProjectGroup,
    Repository,
    SonarQube,
    UnitTest,
)

ENV_FILE = Path(".env")


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def get_url():
    print(f"env file: {ENV_FILE.exists()}")
    if ENV_FILE.exists():
        load_dotenv(ENV_FILE)
        print("Alembinc used local env file.")
    user = os.getenv("POSTGRESQL_USER", "postgres")
    password = os.getenv("POSTGRESQL_PASSWORD", "")
    server = os.getenv("POSTGRESQL_SERVER", "db")
    db = os.getenv("POSTGRESQL_DATABASE", "app")
    return f"postgresql://{user}:{password}@{server}/{db}"


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = get_url()
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
