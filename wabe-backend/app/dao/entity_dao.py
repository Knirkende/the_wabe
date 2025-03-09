from sqlalchemy import select
from app.dao.persistence_config import transactional
from app.model.archetypes import DynamicEntity, Terrain
from sqlalchemy.orm import Session
from typing import Any

class WabeDao:

    def __init__(self):
        pass

    def persist(self, entity, **kwargs):
        """Persist an entity managed by ORM."""
        return self.do_persist(entity=entity, **kwargs)
    
    @transactional
    def do_persist(self, session: Session, entity: DynamicEntity, **kwargs):
        return session.add(entity)

class DynamicEntityDao(WabeDao):
    """Kwargs are consumed by transactional decorator."""

    def __init__(self):
        pass

    def get_all_of_class_type(self, entity_class, **kwargs):
        """Get all rows of an entity type managed by ORM."""
        return self.do_get_all_of_class_type(entity_class = entity_class, **kwargs)
    
    def get_all_at_coordinates(self, y_pos, x_pos, **kwargs):
        """Get all entities at given coordinates."""
        return self.do_get_all_at_coordinates(y_pos=y_pos, x_pos=x_pos, **kwargs)

    @transactional
    def do_get_all_of_class_type(self, session: Session, entity_class: Any, **kwargs):
        return session.scalars(select(entity_class)).fetchall()
    
    @transactional
    def do_get_all_at_coordinates(self, session: Session, y_pos: int, x_pos : int, **kwargs):
        return session.scalars(select(DynamicEntity)
                               .where(DynamicEntity.y_pos == y_pos)
                               .where(DynamicEntity.x_pos == x_pos)).fetchall()

class TerrainDao(WabeDao):

    def __init__(self):
        pass

    def get_single_tile_at_coordinates(self, x_pos, y_pos):
        return self.do_get_single_tile_at_coordinates(x_pos=x_pos, y_pos=y_pos)

    def get_biome(self):
        #TODO implement in service layer
        pass

    @transactional
    def do_get_single_tile_at_coordinates(self, session: Session, y_pos: int, x_pos : int, **kwargs):
        return session.scalar(select(Terrain)
                              .where(Terrain.y_pos == y_pos)
                              .where(Terrain.x_pos == x_pos))