# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0005_auto_20150406_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='extension',
            field=models.CharField(default='cpp', max_length=10),
            preserve_default=False,
        ),
    ]
