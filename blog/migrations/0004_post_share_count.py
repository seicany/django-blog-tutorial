# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-17 03:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_comments_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='share_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
