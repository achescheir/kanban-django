# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 18:49
from __future__ import unicode_literals

from django.db import migrations, models
import tasklist.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('BL', 'Backlog'), ('RD', 'Ready'), ('DO', 'Doing'), ('DN', 'Done')], default='BL', max_length=2)),
                ('priority', models.IntegerField(default=tasklist.models.TaskItem.get_next_priority, unique=True)),
            ],
        ),
    ]
