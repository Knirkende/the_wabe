from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://test_user:test_pw@0.0.0.0/test_db")

def get_scoped_session(bind):
    return scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=bind, expire_on_commit=False))

engine = create_engine(DATABASE_URL)
SessionLocal = get_scoped_session(engine)

def transactional(func):
    def wrapper(*args, **kwargs):
        session = kwargs.pop('session', SessionLocal())
        try:
            result = func(session, *args, **kwargs)
            session.commit()
            if result is not None:
                session.expunge_all()
            return result
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()
    return wrapper