from app.model.animals import Tove, Borogove
from app.dao.entity_dao import persist, get_all_of_class_type
from test.persistence_test_config import *

def test_persist_tove(mock_pg_session):
    t = Tove(
        given_name = 'Johnny',
        x_pos = 0,
        y_pos = 0
        )
    persist(t, session = mock_pg_session)
    res = get_all_of_class_type(t.__class__, session = mock_pg_session)

    assert(res[0].given_name == 'Johnny')

def test_get_all_of_class_type(mock_pg_session):
    t = Tove(
        given_name = 'Johnny',
        x_pos = 0,
        y_pos = 0
        )
    b = Borogove(
        given_name = 'Jackie',
        x_pos = 0,
        y_pos = 0
        )
    persist(t, session = mock_pg_session)
    persist(b, session = mock_pg_session)

    res = get_all_of_class_type(t.__class__, session = mock_pg_session)

    assert(len(res) == 1)
    assert(res[0].given_name == 'Johnny')