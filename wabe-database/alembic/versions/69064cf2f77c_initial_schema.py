"""initial schema

Revision ID: 69064cf2f77c
Revises: 
Create Date: 2025-03-01 19:23:58.798545

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '69064cf2f77c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'dynamic_entity',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('entity_type', sa.String(10), nullable=False),
        sa.Column('given_name', sa.String(10)),
        sa.Column('x_pos', sa.Integer, nullable=False),
        sa.Column('y_pos', sa.Integer, nullable=False),
        sa.Column('condition', sa.Integer(), nullable=False),
        sa.Column('activated', sa.Boolean),
        sa.Column('locked_by', sa.String(32)),
        sa.Column('locked_timestamp', sa.DateTime)
    )
    op.create_table(
        'terrain',
            sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
            sa.Column('terrain_type', sa.String(10), nullable=False),
            sa.Column('x_pos', sa.Integer, nullable=False),
            sa.Column('y_pos', sa.Integer, nullable=False),
            sa.Column('condition', sa.Integer(), nullable=False)
    )
    op.create_unique_constraint('uq_xpos_ypos', 'terrain', ['x_pos', 'y_pos'])

def downgrade() -> None:
    op.drop_table('dynamic_entity')
    op.drop_table('terrain')
    op.drop_constraint(constraint_name='uq_xpos_ypos', table_name='terrain', type_='unique')
