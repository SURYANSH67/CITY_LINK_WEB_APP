"""Increase length of ticket_id column in complaints table

Revision ID: b7bd2c6f0b27
Revises: 3569b05ee918
Create Date: 2025-06-06 13:32:08.910489

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b7bd2c6f0b27'
down_revision = '3569b05ee918'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('complaints', schema=None) as batch_op:
        batch_op.alter_column('ticket_id',
               existing_type=mysql.VARCHAR(length=20),
               type_=sa.String(length=32),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('complaints', schema=None) as batch_op:
        batch_op.alter_column('ticket_id',
               existing_type=sa.String(length=32),
               type_=mysql.VARCHAR(length=20),
               existing_nullable=False)

    # ### end Alembic commands ###
