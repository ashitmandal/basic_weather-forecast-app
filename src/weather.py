
import requests

def get_coordinates(city):
    """Find latitude and longitude for a city."""

    url = "https://geocoding-api.open-meteo.com/v1/search"

    response = requests.get(
        url,
        params={
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        },
        timeout=10
    )

    response.raise_for_status()
    data = response.json()

    if not data.get("results"):
        raise ValueError(f"City not found: {city}")

    location = data["results"][0]
    print(location["latitude"], location["longitude"])

    return location["latitude"], location["longitude"]


def get_weather(city):
    """Fetch current weather for a city."""

    latitude, longitude = get_coordinates(city)

    url = "https://api.open-meteo.com/v1/forecast"

    response = requests.get(
        url,
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
        },
        timeout=10
    )

    response.raise_for_status()

    return response.json()["current"]
