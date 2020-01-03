"""baseline

Revision ID: a6b2f7637738
Revises: 
Create Date: 2020-01-03 17:07:36.570375

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a6b2f7637738'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('org_member',
    sa.Column('row_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('org_uuid', sa.VARCHAR(length=128), nullable=True),
    sa.Column('role', sa.VARCHAR(length=128), nullable=True),
    sa.Column('username', sa.VARCHAR(length=128), nullable=True),
    sa.PrimaryKeyConstraint('row_id')
    )
    op.create_table('organization',
    sa.Column('row_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=128), nullable=False),
    sa.Column('org_uuid', sa.VARCHAR(length=128), nullable=True),
    sa.Column('org_id', sa.VARCHAR(length=128), nullable=False),
    sa.Column('type', sa.VARCHAR(length=128), nullable=False),
    sa.Column('description', sa.VARCHAR(length=1024), nullable=False),
    sa.Column('short_description', sa.VARCHAR(length=1024), nullable=False),
    sa.Column('url', sa.VARCHAR(length=512), nullable=False),
    sa.Column('duns_no', sa.VARCHAR(length=20), nullable=True),
    sa.Column('contacts', mysql.JSON(), nullable=False),
    sa.Column('assets', mysql.JSON(), nullable=False),
    sa.Column('metadata_ipfs_hash', sa.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('row_id')
    )
    op.create_table('organization_history',
    sa.Column('row_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=128), nullable=False),
    sa.Column('org_uuid', sa.VARCHAR(length=128), nullable=True),
    sa.Column('org_id', sa.VARCHAR(length=128), nullable=False),
    sa.Column('type', sa.VARCHAR(length=128), nullable=False),
    sa.Column('description', sa.VARCHAR(length=1024), nullable=False),
    sa.Column('short_description', sa.VARCHAR(length=1024), nullable=False),
    sa.Column('url', sa.VARCHAR(length=512), nullable=False),
    sa.Column('duns_no', sa.VARCHAR(length=20), nullable=True),
    sa.Column('contacts', mysql.JSON(), nullable=False),
    sa.Column('assets', mysql.JSON(), nullable=False),
    sa.Column('metadata_ipfs_hash', sa.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('row_id')
    )
    op.create_table('organization_review_workflow',
    sa.Column('row_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('organization_row_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.VARCHAR(length=128), nullable=False),
    sa.Column('transaction_hash', sa.VARCHAR(length=128), nullable=True),
    sa.Column('user_address', sa.VARCHAR(length=128), nullable=True),
    sa.Column('created_by', sa.VARCHAR(length=128), nullable=False),
    sa.Column('updated_by', sa.VARCHAR(length=128), nullable=False),
    sa.Column('approved_by', sa.VARCHAR(length=128), nullable=True),
    sa.Column('created_on', mysql.TIMESTAMP(), nullable=True),
    sa.Column('updated_on', mysql.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('row_id')
    )
    op.create_table('group',
    sa.Column('row_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=128), nullable=False),
    sa.Column('id', sa.VARCHAR(length=128), nullable=False),
    sa.Column('org_uuid', sa.VARCHAR(length=128), nullable=True),
    sa.Column('org_row_id', sa.Integer(), nullable=False),
    sa.Column('payment_address', sa.VARCHAR(length=128), nullable=False),
    sa.Column('payment_config', mysql.JSON(), nullable=False),
    sa.Column('status', sa.VARCHAR(length=128), nullable=True),
    sa.ForeignKeyConstraint(['org_row_id'], ['organization.row_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('row_id')
    )
    op.create_table('group_history',
    sa.Column('row_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=128), nullable=False),
    sa.Column('id', sa.VARCHAR(length=128), nullable=False),
    sa.Column('org_uuid', sa.VARCHAR(length=128), nullable=True),
    sa.Column('org_row_id', sa.Integer(), nullable=False),
    sa.Column('payment_address', sa.VARCHAR(length=128), nullable=False),
    sa.Column('payment_config', mysql.JSON(), nullable=False),
    sa.Column('status', sa.VARCHAR(length=128), nullable=True),
    sa.ForeignKeyConstraint(['org_row_id'], ['organization_history.row_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('row_id')
    )
    op.create_table('organization_address',
    sa.Column('row_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('org_row_id', sa.Integer(), nullable=False),
    sa.Column('address_type', sa.VARCHAR(length=64), nullable=False),
    sa.Column('street_address', sa.VARCHAR(length=256), nullable=False),
    sa.Column('apartment', sa.VARCHAR(length=256), nullable=False),
    sa.Column('city', sa.VARCHAR(length=64), nullable=False),
    sa.Column('pincode', sa.Integer(), nullable=False),
    sa.Column('state', sa.VARCHAR(length=64), nullable=True),
    sa.Column('country', sa.VARCHAR(length=64), nullable=False),
    sa.Column('created_on', mysql.TIMESTAMP(), nullable=True),
    sa.Column('updated_on', mysql.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['org_row_id'], ['organization.row_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('row_id')
    )
    op.create_table('organization_address_history',
    sa.Column('row_id', sa.Integer(), nullable=False),
    sa.Column('org_row_id', sa.Integer(), nullable=False),
    sa.Column('address_type', sa.VARCHAR(length=64), nullable=False),
    sa.Column('street_address', sa.VARCHAR(length=256), nullable=False),
    sa.Column('apartment', sa.VARCHAR(length=256), nullable=False),
    sa.Column('city', sa.VARCHAR(length=64), nullable=False),
    sa.Column('pincode', sa.Integer(), nullable=False),
    sa.Column('state', sa.VARCHAR(length=64), nullable=True),
    sa.Column('country', sa.VARCHAR(length=64), nullable=False),
    sa.Column('created_on', mysql.TIMESTAMP(), nullable=True),
    sa.Column('updated_on', mysql.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['org_row_id'], ['organization_history.row_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('row_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('organization_address_history')
    op.drop_table('organization_address')
    op.drop_table('group_history')
    op.drop_table('group')
    op.drop_table('organization_review_workflow')
    op.drop_table('organization_history')
    op.drop_table('organization')
    op.drop_table('org_member')
    # ### end Alembic commands ###
