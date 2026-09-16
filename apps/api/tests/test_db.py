import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base
from app.db.session import SessionLocal, engine, get_db
from app.config import settings

def test_database_url_configuration():
    assert "postgresql" in settings.DATABASE_URL

def test_engine_and_session_factory_created():
    assert engine is not None
    assert SessionLocal is not None

def test_base_metadata_exists():
    assert hasattr(Base, "metadata")

def test_get_db_yields_session():
    db_gen = get_db()
    session = next(db_gen)
    assert session is not None
    # We do not actually query to avoid needing a real connection
    session.close()
