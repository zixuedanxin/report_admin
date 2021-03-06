"""Initial migration

Revision ID: 0db24df00b62
Revises: 
Create Date: 2017-09-12 19:43:52.089738

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0db24df00b62'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('weather')
    op.drop_table('bar1')
    op.drop_table('bubble_gradient')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bubble_gradient',
    sa.Column('year', sa.INTEGER(), nullable=True),
    sa.Column('county', sa.TEXT(), nullable=True),
    sa.Column('population', sa.INTEGER(), nullable=True),
    sa.Column('age', sa.INTEGER(), nullable=True)
    )
    op.create_table('bar1',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=True),
    sa.Column('amount', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('weather',
    sa.Column('month', sa.TEXT(), nullable=True),
    sa.Column('evaporation', sa.TEXT(), nullable=True),
    sa.Column('precipitation', sa.TEXT(), nullable=True)
    )
    # ### end Alembic commands ###
