#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""Add description field to connection

Revision ID: 61ec73d9401f
Revises: 2c6edca13270
Create Date: 2020-09-10 14:56:30.279248

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '61ec73d9401f'
down_revision = '2c6edca13270'
branch_labels = None
depends_on = None


def upgrade():
    """Apply Add description field to connection"""
    with op.batch_alter_table('connection') as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(length=5000), nullable=True))


def downgrade():
    """Unapply Add description field to connection"""
    with op.batch_alter_table('connection', schema=None) as batch_op:
        batch_op.drop_column('description')
