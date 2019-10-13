# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-11 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WordFrequency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=2000, unique=True)),
                ('frequency', models.IntegerField(default=0)),
            ],
        ),
    ]
