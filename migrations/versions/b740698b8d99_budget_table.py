"""budget table

Revision ID: b740698b8d99
Revises: 1b6f3a35479a
Create Date: 2022-10-03 19:34:25.223159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b740698b8d99'
down_revision = '1b6f3a35479a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('budget',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('budgettitle', sa.String(length=100), nullable=True),
    sa.Column('budgetamount', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('budget')
    # ### end Alembic commands ###