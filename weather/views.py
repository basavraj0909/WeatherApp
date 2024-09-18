from django.shortcuts import render
from .models import Weather
from .services import get_weather_data

from django.http import JsonResponse
from .models import Weather
from .services import get_weather_data


def fetch_weather(request, city):
    data = get_weather_data(city)
    if data:
        weather = Weather(
            city=data['location']['name'],
            temperature=data['current']['temp_c'],
            humidity=data['current']['humidity'],
            wind_speed=data['current']['wind_kph'],
            description=data['current']['condition']['text']
        )
        weather.save()

        alert = check_for_alerts(weather)

        response_data = {
            'weather': {
                'city': weather.city,
                'temperature': weather.temperature,
                'humidity': weather.humidity,
                'wind_speed': weather.wind_speed,
                'description': weather.description
            },
            'alert': alert
        }
        return JsonResponse(response_data)

    return JsonResponse({'error': 'Could not fetch weather data'})


def check_for_alerts(weather):
    """
    Checks if the weather conditions are extreme and returns an alert message if they are.

    This function evaluates the weather conditions and returns an alert if the temperature
    exceeds 40°C or the wind speed exceeds 100 kph.
    Args:
        weather (Weather): An instance of the Weather model with weather data.

    Returns:
        str: An alert message if extreme conditions are detected, otherwise None.
    """
    if weather.temperature > 40 or weather.wind_speed > 100:
        return "Extreme weather alert!"
    return None
