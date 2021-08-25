"""Save Tables

Revision ID: 41b0dd1d15f6
Revises: 8417bcffd2dc
Create Date: 2021-08-25 16:05:07.799448

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41b0dd1d15f6'
down_revision = '8417bcffd2dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('pp', sa.String(length=55), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'pp')
    # ### end Alembic commands ###
