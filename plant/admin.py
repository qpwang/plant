# -*- coding: utf-8 -*-
from django.contrib import admin
from plant.models import Plant


class PlantAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'kind',
        'status',
        'birthdate',
        'temperature',
        'humidty',
        'sensor_id'
    )

admin.site.register(Plant, PlantAdmin)
