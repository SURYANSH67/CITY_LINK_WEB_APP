"""Add admin_notes to Complaint model

Revision ID: c67a2d193a4c
Revises: b7bd2c6f0b27
Create Date: 2025-06-06 14:23:03.855496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c67a2d193a4c'
down_revision = 'b7bd2c6f0b27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('complaints', schema=None) as batch_op:
        batch_op.add_column(sa.Column('admin_notes', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('complaints', schema=None) as batch_op:
        batch_op.drop_column('admin_notes')

    # ### end Alembic commands ###
