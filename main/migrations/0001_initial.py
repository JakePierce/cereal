# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cereal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('hc', models.CharField(max_length=3, null=True, blank=True)),
                ('cals', models.FloatField(max_length=30, null=True, blank=True)),
                ('protein', models.FloatField(max_length=30, null=True, blank=True)),
                ('fat', models.FloatField(max_length=30, null=True, blank=True)),
                ('sodium', models.FloatField(max_length=30, null=True, blank=True)),
                ('fiber', models.FloatField(max_length=30, null=True, blank=True)),
                ('carbs', models.FloatField(max_length=30, null=True, blank=True)),
                ('sugs', models.FloatField(max_length=30, null=True, blank=True)),
                ('potass', models.FloatField(max_length=30, null=True, blank=True)),
                ('vits', models.FloatField(max_length=30, null=True, blank=True)),
                ('weight', models.FloatField(max_length=30, null=True, blank=True)),
                ('cups', models.FloatField(max_length=30, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='cereal',
            name='manufacturer',
            field=models.ForeignKey(blank=True, to='main.Manufacturer', null=True),
        ),
    ]
