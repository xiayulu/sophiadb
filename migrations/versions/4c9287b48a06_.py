"""empty message

Revision ID: 4c9287b48a06
Revises: 8be2fd523fca
Create Date: 2021-01-23 09:48:16.980267

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c9287b48a06'
down_revision = '8be2fd523fca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('file',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('file_type', sa.String(), nullable=True),
    sa.Column('file_url', sa.String(), nullable=False),
    sa.Column('created_time', sa.DateTime(), nullable=True),
    sa.Column('updated_time', sa.DateTime(), nullable=True),
    sa.Column('file_size', sa.Float(), nullable=True),
    sa.Column('file_info', sa.String(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('contribute',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('file_id', sa.Integer(), nullable=False),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['file_id'], ['file.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'file_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contribute')
    op.drop_table('file')
    # ### end Alembic commands ###
