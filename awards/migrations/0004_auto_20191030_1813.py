# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-30 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0003_auto_20191030_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='content',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)], default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='design',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)], default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='usability',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)], default=0),
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
