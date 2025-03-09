from sqlalchemy import select
from app.dao.persistence_config import transactional




def persist(entity, **kwargs):
    """Persist an entity managed by ORM. Kwargs are consumed by transactional decorator."""
    return do_persist(entity=entity, **kwargs)

def get_all_of_class_type(entity_class, **kwargs):
    """Get all rows of an entity type managed by ORM. Kwargs are consumed by transactional decorator."""
    return do_get_all_of_class_type(entity_class = entity_class, **kwargs)

@transactional
def do_persist(session, entity, **kwargs):
    return session.add(entity)

@transactional
def do_get_all_of_class_type(session, entity_class, **kwargs):
    return session.scalars(select(entity_class)).fetchall()