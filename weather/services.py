import requests
from django.conf import settings

# Use the configuration values from settings.py
API_KEY = settings.API_KEY
print('API_KEY', API_KEY)
BASE_URL = settings.BASE_URL
print('BASE_URL', BASE_URL)

def get_weather_data(city):
    """
    Fetches real-time weather data for a given city using the Weather API.

    Args:
        city (str): The name of the city for which to fetch weather data.

    Returns:
        dict: A dictionary containing the weather data if the request is successful.
        None: If there is an error fetching the data.

    Raises:
        requests.exceptions.RequestException: If an error occurs during the request.
    """
    try:
        # Construct the URL for the API request
        url = f'{BASE_URL}?key={API_KEY}&q={city}'
        print(f"Request URL: {url}")

        # Send a GET request to the API
        response = requests.get(url)

        # Raise an exception for HTTP error responses
        response.raise_for_status()

        # Return the JSON response
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
