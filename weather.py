# - Create a Python script that fetches data
#  from a public API (e.g., OpenWeatherMap) 
# and displays the weather.

import json, requests



api_key = "f9abb0a365aaa92adbebda1b533045b5"

location = input("Enter location: ")


url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

response = requests.get(url)
response.raise_for_status()

# weather_data = json.loads(response.text)
weather_data = response.json()

print(f"The weather in {location} is {weather_data['weather'][0]['description']}")
