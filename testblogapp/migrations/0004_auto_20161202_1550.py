# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-02 12:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testblogapp', '0003_auto_20161202_1537'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subscribe',
            unique_together=set([]),
        ),
    ]