from django.db import models
from django.contrib.gis.db import models as gis_models  # optional: if you need spatial queries

class MarineWeather(models.Model):
    # Optional: if you need geospatial queries, use GeoDjango’s PointField
    # location = gis_models.PointField(null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    forecast_time = models.DateTimeField()  # the time of the forecast
    wave_height = models.FloatField(null=True, blank=True)       # in meters
    wind_wave_height = models.FloatField(null=True, blank=True)  # in meters
    swell_wave_height = models.FloatField(null=True, blank=True) # in meters
    sea_surface_temperature = models.FloatField(null=True, blank=True)  # in Celsius

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Forecast at {self.forecast_time} for ({self.latitude}, {self.longitude})"
