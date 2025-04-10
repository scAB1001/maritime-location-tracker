import requests
from celery import shared_task
from django.conf import settings
from datetime import datetime
from .models import MarineWeather

@shared_task
def fetch_marine_weather():
    url = "https://marine-api.open-meteo.com/v1/marine"
    params = {
        "latitude": settings.WEATHER_LATITUDE,    # e.g., 54.544587
        "longitude": settings.WEATHER_LONGITUDE,   # e.g., 10.227487
        "hourly": "wave_height,wind_wave_height,swell_wave_height,sea_surface_temperature",
        "forecast_days": 7,
        "timezone": "GMT",
    }
    
    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print("Error fetching marine weather data:", e)
        return

    # For demonstration, assume data['hourly'] contains arrays for time and variables.
    times = data.get("hourly", {}).get("time", [])
    wave_heights = data.get("hourly", {}).get("wave_height", [])
    wind_wave_heights = data.get("hourly", {}).get("wind_wave_height", [])
    swell_wave_heights = data.get("hourly", {}).get("swell_wave_height", [])
    sea_surface_temps = data.get("hourly", {}).get("sea_surface_temperature", [])
    
    for i, time_str in enumerate(times):
        try:
            forecast_time = datetime.fromisoformat(time_str)
        except ValueError:
            continue
        
        # Save each forecast record (you could also bulk create for efficiency)
        MarineWeather.objects.create(
            latitude=float(params["latitude"]),
            longitude=float(params["longitude"]),
            forecast_time=forecast_time,
            wave_height=wave_heights[i] if i < len(wave_heights) else None,
            wind_wave_height=wind_wave_heights[i] if i < len(wind_wave_heights) else None,
            swell_wave_height=swell_wave_heights[i] if i < len(swell_wave_heights) else None,
            sea_surface_temperature=sea_surface_temps[i] if i < len(sea_surface_temps) else None,
        )
