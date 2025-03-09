from sqlalchemy import select
from app.dao.persistence_config import transactional
from app.model.archetypes import DynamicEntity
from sqlalchemy.orm import Session
from typing import Any

class DynamicEntityDao:

    def __init__(self):
        pass

    def persist(self, entity, **kwargs):
        """Persist an entity managed by ORM. Kwargs are consumed by transactional decorator."""
        print(self, entity)
        return self.do_persist(entity=entity, **kwargs)

    def get_all_of_class_type(self, entity_class, **kwargs):
        """Get all rows of an entity type managed by ORM. Kwargs are consumed by transactional decorator."""
        return self.do_get_all_of_class_type(entity_class = entity_class, **kwargs)
    
    def get_all_at_coordinates(self, y_pos, x_pos, **kwargs):
        """Get all entities at given coordinates. Kwargs are consumed by transactional decorator."""
        return self.do_get_all_at_coordinates(y_pos=y_pos, x_pos=x_pos, **kwargs)

    @transactional
    def do_persist(self, session: Session, entity: DynamicEntity, **kwargs):
        print(self, session, entity)
        return session.add(entity)

    @transactional
    def do_get_all_of_class_type(self, session: Session, entity_class: Any, **kwargs):
        return session.scalars(select(entity_class)).fetchall()
    
    @transactional
    def do_get_all_at_coordinates(self, session: Session, y_pos: int, x_pos : int, **kwargs):
        return session.scalars(select(DynamicEntity)
                               .where(DynamicEntity.y_pos == y_pos)
                               .where(DynamicEntity.x_pos == x_pos)).fetchall()