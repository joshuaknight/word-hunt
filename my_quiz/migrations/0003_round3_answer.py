# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-07 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_quiz', '0002_round3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Round3_answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('input', models.CharField(max_length=200)),
                ('correct', models.CharField(max_length=200)),
            ],
        ),
    ]
