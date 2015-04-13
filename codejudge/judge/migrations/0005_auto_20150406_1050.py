# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0004_auto_20150406_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='constraints',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='problem',
            name='outputFormat',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='problem',
            name='problemStatement',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='problem',
            name='sampleInput',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='problem',
            name='sampleOutput',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
