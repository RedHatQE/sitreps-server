"""DB session generator."""

from collections.abc import Generator

from ...db import SessionLocal


def get_db() -> Generator:
    """Get db session."""
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
