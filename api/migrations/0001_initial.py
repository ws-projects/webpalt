# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-05 05:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='no_name', max_length=100, verbose_name='\u59d3\u540d')),
                ('sex', models.CharField(default='male', max_length=50, verbose_name='\u6027\u522b')),
                ('sid', models.CharField(default='0', max_length=100, verbose_name='\u5b66\u53f7')),
            ],
        ),
    ]
