from rest_framework import serializers
from .models import MarineWeather

class MarineWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarineWeather
        fields = '__all__'
