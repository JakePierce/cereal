# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20151013_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cereal',
            name='manufacturer',
            field=models.ForeignKey(null=True, blank=True, to='main.Manufacturer', unique=True),
        ),
    ]
