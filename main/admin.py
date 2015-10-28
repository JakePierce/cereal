from django.contrib import admin
from main.models import Cereal, Manufacturer
from django import forms


class CerealAdmin(admin.ModelAdmin):
    list_display = ('name', 'cals', 'protein')
    search_fields = ['name']


admin.site.register(Cereal, CerealAdmin)
admin.site.register(Manufacturer)
# Register your models here.
