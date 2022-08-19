"""merge 37c 187

Revision ID: 319cfa110371
Revises: 37cddbf6b1c7, 1870f9c2051e
Create Date: 2022-08-19 14:37:52.693042

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '319cfa110371'
down_revision = ('37cddbf6b1c7', '1870f9c2051e')
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
