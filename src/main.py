
from src.weather import get_weather


def main():
    city = input("Enter city name: ").strip()

    try:
        weather = get_weather(city)

        print("\n===== LIVE WEATHER REPORT =====")
        print(f"City        : {city}")
        print(f"Temperature : {weather['temperature_2m']} C")
        print(f"Humidity    : {weather['relative_humidity_2m']}%")
        print(f"Wind Speed  : {weather['wind_speed_10m']} km/h")

    except (ValueError, KeyError) as error:
        print(f"Error: {error}")

    except Exception as error:
        print(f"API or network error: {error}")


if __name__ == "__main__":
    main()
