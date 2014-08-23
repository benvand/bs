# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20140823_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='htmlslug',
            name='author_name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='htmlslug',
            name='favicon',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='htmlslug',
            name='home_url_name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='htmlslug',
            name='meta_keywords',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='htmlslug',
            name='path_to_favicon',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
