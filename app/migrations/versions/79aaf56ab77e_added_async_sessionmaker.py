"""Added async sessionmaker

Revision ID: 79aaf56ab77e
Revises: 2f9313503519
Create Date: 2024-02-18 12:38:01.057263

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '79aaf56ab77e'
down_revision: Union[str, None] = '2f9313503519'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###