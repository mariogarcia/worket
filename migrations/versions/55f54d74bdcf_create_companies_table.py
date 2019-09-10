"""create companies table

Revision ID: 55f54d74bdcf
Revises:
Create Date: 2019-09-10 17:27:21.683220

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = '55f54d74bdcf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'companies',
        sa.Column('id', UUID, primary_key=True),
        sa.Column('name', sa.String)
    )


def downgrade():
    pass
