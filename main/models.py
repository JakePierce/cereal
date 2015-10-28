from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=True)


    def __unicode__(self):
        return self.name


class Cereal(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=True)
    manufacturer = models.ForeignKey('main.Manufacturer', null=True, blank=True)
    hc = models.CharField(max_length=3, null=True, blank=True)
    cals = models.FloatField(max_length=30, null=True, blank=True)
    protein = models.FloatField(max_length=30, null=True, blank=True)
    fat = models.FloatField(max_length=30, null=True, blank=True)
    sodium = models.FloatField(max_length=30, null=True, blank=True)
    fiber = models.FloatField(max_length=30, null=True, blank=True)
    carbs = models.FloatField(max_length=30, null=True, blank=True)
    sugs = models.FloatField(max_length=30, null=True, blank=True)
    potass = models.FloatField(max_length=30, null=True, blank=True)
    vits = models.FloatField(max_length=30, null=True, blank=True)
    weight = models.FloatField(max_length=30, null=True, blank=True)
    cups = models.FloatField(max_length=30, null=True, blank=True)


    def __unicode__(self):
        return self.name
