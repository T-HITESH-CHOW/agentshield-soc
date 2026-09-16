"""Add Alert model

Revision ID: 3cdff330a6c0
Revises: 
Create Date: 2026-09-16 17:09:29.832717

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3cdff330a6c0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'alerts',
        sa.Column('id', sa.Uuid(), nullable=False),
        sa.Column('external_id', sa.String(length=255), nullable=True),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('severity', sa.Enum('LOW', 'MEDIUM', 'HIGH', 'CRITICAL', name='alertseverity', native_enum=False), nullable=False),
        sa.Column('status', sa.Enum('NEW', 'ACKNOWLEDGED', 'INVESTIGATING', 'RESOLVED', 'FALSE_POSITIVE', name='alertstatus', native_enum=False), nullable=False),
        sa.Column('source', sa.String(length=255), nullable=False),
        sa.Column('source_type', sa.String(length=255), nullable=True),
        sa.Column('detected_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('source_ip', sa.String(length=50), nullable=True),
        sa.Column('destination_ip', sa.String(length=50), nullable=True),
        sa.Column('hostname', sa.String(length=255), nullable=True),
        sa.Column('username', sa.String(length=255), nullable=True),
        sa.Column('detection_rule', sa.String(length=255), nullable=True),
        sa.Column('mitre_technique', sa.String(length=50), nullable=True),
        sa.Column('raw_event', sa.JSON(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_alerts_detected_at'), 'alerts', ['detected_at'], unique=False)
    op.create_index(op.f('ix_alerts_external_id'), 'alerts', ['external_id'], unique=False)
    op.create_index(op.f('ix_alerts_hostname'), 'alerts', ['hostname'], unique=False)
    op.create_index(op.f('ix_alerts_severity'), 'alerts', ['severity'], unique=False)
    op.create_index(op.f('ix_alerts_source'), 'alerts', ['source'], unique=False)
    op.create_index(op.f('ix_alerts_source_ip'), 'alerts', ['source_ip'], unique=False)
    op.create_index(op.f('ix_alerts_status'), 'alerts', ['status'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_alerts_status'), table_name='alerts')
    op.drop_index(op.f('ix_alerts_source_ip'), table_name='alerts')
    op.drop_index(op.f('ix_alerts_source'), table_name='alerts')
    op.drop_index(op.f('ix_alerts_severity'), table_name='alerts')
    op.drop_index(op.f('ix_alerts_hostname'), table_name='alerts')
    op.drop_index(op.f('ix_alerts_external_id'), table_name='alerts')
    op.drop_index(op.f('ix_alerts_detected_at'), table_name='alerts')
    op.drop_table('alerts')
