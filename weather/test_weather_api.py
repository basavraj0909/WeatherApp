import requests
import logging
import sys

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Define the base URL for your Django application
BASE_URL = 'http://127.0.0.1:8000'  # Replace with your deployed URL if testing on Render


def test_fetch_weather(city):
    """
    Test the fetch_weather API endpoint for a given city.

    Args:
        city (str): The name of the city to test.

    Returns:
        None
    """
    url = f'{BASE_URL}/weather/{city}/'  # Adjust the endpoint URL if needed

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad HTTP status codes

        logger.info(f"Request URL: {url}")
        logger.info(f"Status Code: {response.status_code}")

        # Try parsing the JSON response
        try:
            data = response.json()
            logger.info("Response Data: %s", data)

            if response.status_code == 200:
                if 'weather' in data:
                    print("Weather data received:")
                    print(f"City: {data['weather'].get('city')}")
                    print(f"Temperature: {data['weather'].get('temperature')}")
                    print(f"Humidity: {data['weather'].get('humidity')}")
                    print(f"Wind Speed: {data['weather'].get('wind_speed')}")
                    print(f"Description: {data['weather'].get('description')}")
                elif 'error' in data:
                    logger.error("Error parsing JSON: %s", e)
                    print("Error message:", data['error'])
                else:
                    print("Unexpected response format")
            else:
                print("Failed to fetch weather data")
        except ValueError as e:
            logger.error("Error parsing JSON: %s", e)
            return None

    except requests.exceptions.RequestException as e:
        logger.error("Error during request: %s", e)




if __name__ == "__main__":
    # Replace with actual city names for testing
    # test_fetch_weather('Mumbai')
    test_fetch_weather('New York')

