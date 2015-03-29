# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('commentText', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contestName', models.CharField(unique=True, max_length=200)),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hacker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hackerName', models.CharField(unique=True, max_length=200)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('password', models.CharField(max_length=200)),
                ('collegeName', models.CharField(max_length=200)),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to=b'avatar')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('problemSetter', models.CharField(max_length=200)),
                ('problemTitle', models.CharField(max_length=200)),
                ('problemStatement', models.TextField()),
                ('testInput', models.FileField(upload_to=b'testInput')),
                ('testOutput', models.FileField(upload_to=b'testOutput')),
                ('points', models.PositiveSmallIntegerField()),
                ('timeLimit', models.PositiveSmallIntegerField()),
                ('languagesAllowed', models.CommaSeparatedIntegerField(max_length=200)),
                ('solvedBy', models.PositiveSmallIntegerField(default=0)),
                ('contest', models.ForeignKey(to='judge.Contest')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('points', models.PositiveSmallIntegerField()),
                ('solution', models.TextField()),
                ('attempts', models.PositiveSmallIntegerField()),
                ('time', models.DecimalField(max_digits=2, decimal_places=2)),
                ('contest', models.ForeignKey(to='judge.Contest')),
                ('hacker', models.ForeignKey(to='judge.Hacker')),
                ('language', models.ForeignKey(to='judge.Language')),
                ('problem', models.ForeignKey(to='judge.Problem')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comments',
            name='contest',
            field=models.ForeignKey(to='judge.Contest'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comments',
            name='hacker',
            field=models.ForeignKey(to='judge.Hacker'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comments',
            name='problem',
            field=models.ForeignKey(to='judge.Problem'),
            preserve_default=True,
        ),
    ]
