from rest_framework import viewsets
from .models import MarineWeather
from .serializers import MarineWeatherSerializer

class MarineWeatherViewSet(viewsets.ModelViewSet):
    queryset = MarineWeather.objects.all().order_by('forecast_time')
    serializer_class = MarineWeatherSerializer
