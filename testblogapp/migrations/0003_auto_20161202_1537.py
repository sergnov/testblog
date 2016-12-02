# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-02 12:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testblogapp', '0002_post_append_time'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subscribe',
            unique_together=set([('user', 'blog')]),
        ),
    ]
