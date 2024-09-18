# Weather Data Management Application

This Django application fetches real-time weather data from a public API, processes the data to provide insights, and displays alerts if extreme weather conditions are detected. It uses a configuration file (config.ini) for managing API keys and base URLs.

## Features
    - Fetch real-time weather data for a given city or set of cities.
    - Process weather data to calculate trends (e.g., average temperature).
    - Display alerts for extreme weather conditions.

# Installation

## Prerequisites
    Python 3.8 or higher
    Django 4.x
    requests library


# Usage
 - Fetch Weather Data:
    Access the weather data by visiting http://127.0.0.1:8000/weather/ and provide a city name.

 - View Alerts:
    Alerts will be displayed if the weather conditions are extreme based on predefined thresholds.

## Testing
    - The application includes a test script to verify the functionality of the weather API endpoint. This script uses the `requests` library to send HTTP GET requests to the API and prints out the results.

### Test Script
    The test script `test_weather_api.py` is located in the `weather` directory. This script tests the `fetch_weather` API endpoint for various cities.

## Example Output

Testing city: Mumbai
Status Code: 200
Response Content: {
    "weather": {
        "city": "Mumbai",
        "temperature": "29.2°C",
        "humidity": "70%",
        "wind_speed": "9.7 kph",
        "description": "Mist"
    }
}







weatherapp/
├── weather/ (your app folder)
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py  # We will create this
│   └── templates/
│       └── weather.html  # We will create this
├── weatherapp/ (project folder)
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
