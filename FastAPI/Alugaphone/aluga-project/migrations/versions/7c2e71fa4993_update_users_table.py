"""update_users_table

Revision ID: 7c2e71fa4993
Revises: c125b57618a4
Create Date: 2024-06-27 15:26:51.253906

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7c2e71fa4993'
down_revision: Union[str, None] = 'c125b57618a4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Users', sa.Column('email', sa.String(), nullable=False))
    op.add_column('Users', sa.Column('password', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Users', 'password')
    op.drop_column('Users', 'email')
    # ### end Alembic commands ###
