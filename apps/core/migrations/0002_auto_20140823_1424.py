# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HTMLSlug',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('favicon', models.CharField(max_length=255)),
                ('meta_keywords', models.CharField(max_length=255)),
                ('author_name', models.CharField(max_length=255)),
                ('path_to_favicon', models.CharField(max_length=255)),
                ('home_url_name', models.CharField(max_length=255)),
                ('site', models.OneToOneField(to='sites.Site')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='htmlslugs',
            name='site',
        ),
        migrations.DeleteModel(
            name='HTMLSlugs',
        ),
    ]
