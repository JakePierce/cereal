#!/usr/bin/env python

import csv
import sys
import os

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
# import django
# django.setup()

from main.models import Cereal, Manufacturer
print os.path.abspath(__file__)

dir_name = os.path.dirname(os.path.abspath(__file__))
file_name = "cereal.csv"

cereal_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cereal.csv")
csv_file = open(cereal_csv, 'r')

reader = csv.DictReader(csv_file)

cereals = Cereal.objects.all()

# for cereal in cereals:
#     print cereal.name
for row in reader:
    new_manufacturer, created = Manufacturer.objects.get_or_create(name=row['Manufacturer'])
    new_manufacturer.name = row['Manufacturer']

    new_manufacturer.save()

    new_cereal, created = Cereal.objects.get_or_create(name=row['Cereal Name'])
    new_cereal.manufacturer = new_manufacturer
    new_cereal.hc = row['Type']
    new_cereal.cals = row['Calories']
    new_cereal.protein = row['Protein (g)']
    new_cereal.fat = row['Fat']
    new_cereal.sodium = row['Sodium']
    new_cereal.fiber = row['Dietary Fiber']
    new_cereal.carbs = row['Carbs']
    new_cereal.sugs = row['Sugars']
    new_cereal.shelf = row['Display Shelf']
    new_cereal.potass = row['Potassium']
    new_cereal.vits = row['Vitamins and Minerals']
    new_cereal.weight = row['Serving Size Weight']
    new_cereal.cups = row['Cups per Serving']

    new_cereal.save()

csv_file.close()
