from django.contrib import admin
from .models import MarineWeather

@admin.register(MarineWeather)
class MarineWeatherAdmin(admin.ModelAdmin):
    list_display = ('forecast_time', 'latitude', 'longitude', 'wave_height', 'sea_surface_temperature')
