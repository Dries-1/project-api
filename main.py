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
print(response)
 
