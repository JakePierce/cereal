# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cereal',
            name='name',
            field=models.CharField(default=1, unique=True, max_length=100, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(unique=True, max_length=255, blank=True),
        ),
    ]
