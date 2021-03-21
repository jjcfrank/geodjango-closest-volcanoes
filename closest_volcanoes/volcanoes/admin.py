from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Volcanoe

@admin.register(Volcanoe)

class VolcanoeAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')