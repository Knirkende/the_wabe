from sqlalchemy import create_engine
from app.dao.persistence_config import get_scoped_session
import pytest

TEST_DATABASE_URL = "postgresql://test_user:test_pw@0.0.0.0/test_db"

@pytest.fixture
def mock_pg_session():
    """yield a postgres session and roll back transaction"""
    engine = create_engine(TEST_DATABASE_URL, echo=True)
    conn = engine.connect()
    trans = conn.begin()
    
    SessionLocal = get_scoped_session(conn)

    session = SessionLocal()

    yield session

    session.close()
    trans.rollback()
    conn.close()