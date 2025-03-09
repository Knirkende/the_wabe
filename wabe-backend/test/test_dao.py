from app.model.animals import Tove, Borogove
from test.persistence_test_config import *
from app.dao.entity_dao import DynamicEntityDao

def test_persist_tove(mock_pg_session, test_dao: DynamicEntityDao):
    t = Tove(
        given_name = 'Johnny',
        x_pos = 0,
        y_pos = 0
        )
    test_dao.persist(t, session = mock_pg_session)
    res = test_dao.get_all_of_class_type(t.__class__, session = mock_pg_session)

    assert(res[0].given_name == 'Johnny')

def test_get_all_of_class_type(mock_pg_session, test_dao: DynamicEntityDao):
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
    test_dao.persist(t, session = mock_pg_session)
    test_dao.persist(b, session = mock_pg_session)

    res = test_dao.get_all_of_class_type(t.__class__, session = mock_pg_session)

    assert(len(res) == 1)
    assert(res[0].given_name == 'Johnny')

def test_get_all_at_coordinates(mock_pg_session, test_dao: DynamicEntityDao):
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
    bb = Borogove(
        given_name = 'Billie',
        x_pos = 1,
        y_pos = 1
        )
    [test_dao.persist(x, session = mock_pg_session) for x in (t, b, bb)]
    res = test_dao.get_all_at_coordinates(0, 0, session = mock_pg_session)

    assert(len(res) == 2)