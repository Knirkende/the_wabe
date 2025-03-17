from sqlalchemy import create_engine
from app.dao.persistence_config import get_scoped_session
from app.dao.entity_dao import DynamicEntityDao, TerrainDao
import pytest
from sqlalchemy.exc import InvalidRequestError

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
    try:
        if trans.is_active:
            trans.rollback()
    except InvalidRequestError:
        pass

    conn.close()

@pytest.fixture
def test_dynamic_dao():
    return DynamicEntityDao()

@pytest.fixture
def test_terrain_dao():
    return TerrainDao()