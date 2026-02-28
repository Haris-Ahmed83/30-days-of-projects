
import requests

def get_weather(city_name):
    base_url = "https://api.open-meteo.com/v1/forecast"
    # Open-Meteo uses latitude and longitude, so we need a way to get that from a city name.
    # For simplicity, we'll use a hardcoded example or a basic geocoding API if available and free.
    # For this example, let's assume we have a way to get lat/lon for a few cities.
    # In a real application, you'd integrate with a geocoding service like OpenStreetMap Nominatim.

    # Example coordinates for a few cities
    city_coordinates = {
        "london": {"latitude": 51.5074, "longitude": 0.1278},
        "new york": {"latitude": 40.7128, "longitude": -74.0060},
        "tokyo": {"latitude": 35.6895, "longitude": 139.6917},
        "sydney": {"latitude": -33.8688, "longitude": 151.2093},
        "paris": {"latitude": 48.8566, "longitude": 2.3522},
    }

    city_name_lower = city_name.lower()

    if city_name_lower not in city_coordinates:
        print(f"Sorry, I don't have coordinates for {city_name}. Please try one of: {', '.join(city_coordinates.keys())}")
        return

    coords = city_coordinates[city_name_lower]
    params = {
        "latitude": coords["latitude"],
        "longitude": coords["longitude"],
        "current_weather": True,
        "temperature_unit": "celsius",
        "windspeed_unit": "kmh",
        "precipitation_unit": "mm",
        "timezone": "auto"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        weather_data = response.json()

        current_weather = weather_data.get("current_weather")
        if current_weather:
            temperature = current_weather.get("temperature")
            windspeed = current_weather.get("windspeed")
            weathercode = current_weather.get("weathercode")

            # Map weather codes to descriptions (simplified for this example)
            weather_descriptions = {
                0: "Clear sky",
                1: "Mostly clear",
                2: "Partly cloudy",
                3: "Overcast",
                45: "Fog",
                48: "Depositing rime fog",
                51: "Drizzle: Light",
                53: "Drizzle: Moderate",
                55: "Drizzle: Dense intensity",
                56: "Freezing Drizzle: Light",
                57: "Freezing Drizzle: Dense intensity",
                61: "Rain: Slight",
                63: "Rain: Moderate",
                65: "Rain: Heavy intensity",
                66: "Freezing Rain: Light",
                67: "Freezing Rain: Heavy intensity",
                71: "Snow fall: Slight",
                73: "Snow fall: Moderate",
                75: "Snow fall: Heavy intensity",
                77: "Snow grains",
                80: "Rain showers: Slight",
                81: "Rain showers: Moderate",
                82: "Rain showers: Violent",
                85: "Snow showers: Slight",
                86: "Snow showers: Heavy",
                95: "Thunderstorm: Slight or moderate",
                96: "Thunderstorm with slight hail",
                99: "Thunderstorm with heavy hail"
            }
            description = weather_descriptions.get(weathercode, "Unknown")

            print(f"Weather in {city_name.title()}:")
            print(f"  Temperature: {temperature}°C")
            print(f"  Windspeed: {windspeed} km/h")
            print(f"  Conditions: {description}")
        else:
            print(f"Could not retrieve current weather for {city_name}.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except ValueError:
        print("Error parsing weather data. Invalid JSON response.")

if __name__ == "__main__":
    while True:
        city = input("Enter city name (or 'exit' to quit): ")
        if city.lower() == 'exit':
            break
        get_weather(city)

