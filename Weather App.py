import requests

# Constants
API_KEY = "API-KEY"  # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """
    Fetch weather details for the given city using OpenWeatherMap API.
    """
    try:
        # Create URL with query parameters (city & API key)
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"  # Get temperature in Celsius
        }
        
        # Send GET request to OpenWeatherMap API
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise exception for bad responses (4xx/5xx)

        # Parse response JSON
        data = response.json()

        # Extract useful information
        city_name = data['name']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Display weather information
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {weather_description.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")

    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except KeyError:
        print("Invalid city name or unexpected data format.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
