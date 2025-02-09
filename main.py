import datetime as dt
import requests

base_url = "http://api.openweathermap.org/data/2.5/weather?"
API_key = "8467dccc7c973e4c667fc1ceb1e57b2c"
city_name = "New York"

def kelvin_to_celsius(temp):
    celcius = temp - 273.15
    return celcius

complete_url = f"{base_url}appid={API_key}&q={city_name}"

response = requests.get(complete_url).json()

temperature = response['main']['temp']
feel_like_kelvin = response['main']['feels_like']
feel_like_celsius = kelvin_to_celsius(feel_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone']).strftime('%H:%M:%S')
sunset = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone']).strftime('%H:%M:%S')

print(response)