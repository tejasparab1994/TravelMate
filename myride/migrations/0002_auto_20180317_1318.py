# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-03-17 17:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myride', '0001_initial'),
        ('offer', '0001_initial'),
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='eid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offer.Enlist'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.User'),
        ),
    ]