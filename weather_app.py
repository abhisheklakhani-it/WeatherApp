import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def fetch_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # For temperature in Celsius. Use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

        # Parse the JSON data
        data = response.json()
        
        # Extract useful information
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }

        return weather

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error occurred: {req_err}")
    except KeyError:
        print("City not found or unexpected response format.")
    
    return None

# Main function to interact with the user
def main():
    api_key = os.getenv("OPENWEATHER_API_KEY")  # Retrieve API key from environment variable

    if not api_key:
        print("Error: API key not found. Please ensure it's set in the .env file.")
        return

    while True:
        city_name = input("Enter city name (or 'exit' to quit): ").strip()
        if city_name.lower() == 'exit':
            break
        
        weather = fetch_weather(city_name, api_key)
        
        if weather:
            print(f"\nWeather in {weather['city']}:")
            print(f"Temperature: {weather['temperature']}°C")
            print(f"Description: {weather['description']}")
            print(f"Humidity: {weather['humidity']}%")
            print(f"Wind Speed: {weather['wind_speed']} m/s\n")
        else:
            print("Could not retrieve weather data. Please try again.\n")

if __name__ == "__main__":
    main()