# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0002_solution_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='constraints',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem',
            name='inputFormat',
            field=models.TextField(default='blank'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem',
            name='outputFormat',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem',
            name='sampleInput',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem',
            name='sampleOutput',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
