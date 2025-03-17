from typing import Optional
from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy import String, DateTime, UniqueConstraint
from sqlalchemy.orm import mapped_column

class PersistenceType(DeclarativeBase):
    pass

class BaseEntity():
    pass
    
class DynamicEntity(BaseEntity, PersistenceType):
    __tablename__ = 'dynamic_entity'

    __mapper_args__ = {
        'polymorphic_identity': 'dynamic_entity',
        'polymorphic_on': 'entity_type'
    }

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, autoincrement=True)
    entity_type: Mapped[str] = mapped_column(String(10), nullable=False)
    given_name: Mapped[str] = mapped_column(String(10))
    x_pos: Mapped[int] = mapped_column(nullable=False)
    y_pos: Mapped[int] = mapped_column(nullable=False)
    condition: Mapped[int] = mapped_column(nullable=False, default=100)
    activated: Mapped[bool] = mapped_column(default=False)
    locked_by: Mapped[Optional[str]] = mapped_column(String(32))
    locked_timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f'DynamicEntity<Id: {self.id}, type: {self.entity_type}>'

class Terrain(BaseEntity, PersistenceType):

    __tablename__ = 'terrain'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, autoincrement=True)
    terrain_type: Mapped[str] = mapped_column(String(10), nullable=False)
    x_pos: Mapped[int] = mapped_column(nullable=False)
    y_pos: Mapped[int] = mapped_column(nullable=False)
    condition: Mapped[int] = mapped_column(default = 0)

    seed_strength: int = 100

    __table_args__ = (
        UniqueConstraint('x_pos', 'y_pos', name='uq_xpos_ypos'),
    )