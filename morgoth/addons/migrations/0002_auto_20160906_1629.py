# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 16:29
# flake8: noqa
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addon',
            name='xpi_filesize',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='addon',
            name='xpi_hash',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='addon',
            name='ftp_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]