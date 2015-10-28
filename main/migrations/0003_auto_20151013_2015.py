# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20151013_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cereal',
            name='manufacturer',
            field=models.ForeignKey(default=1, blank=True, to='main.Manufacturer', unique=True),
            preserve_default=False,
        ),
    ]
