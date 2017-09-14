# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-14 17:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    INDEX_SQL = """
    CREATE INDEX CONCURRENTLY msgs_msg_channel_external_id_not_null
    ON msgs_msg (channel_id, external_id)
    WHERE external_id IS NOT NULL;
    DROP INDEX CONCURRENTLY IF EXISTS msgs_msg_external_id_not_null;
    """

    dependencies = [
        ('msgs', '0103_auto_20170824_1553'),
    ]

    operations = [
        migrations.RunSQL(INDEX_SQL),
    ]
