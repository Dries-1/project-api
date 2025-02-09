import datetime as dt
import requests

def kelvin_to_celsius(temp):
    return temp - 273.15

def get_weather_data(city_name, API_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={API_key}&q={city_name}"
    response = requests.get(complete_url).json()
    return response

def get_temperature(response):
    return kelvin_to_celsius(response['main']['temp'])

def get_wind_speed(response):
    return response['wind']['speed']

def get_humidity(response):
    return response['main']['humidity']

def get_weather_description(response):
    return response['weather'][0]['description']

def get_sunrise_time(response):
    return dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone']).strftime('%H:%M:%S')

def get_sunset_time(response):
    return dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone']).strftime('%H:%M:%S')

if __name__ == "__main__":
    API_key = "8467dccc7c973e4c667fc1ceb1e57b2c"
    
    city_name = input("Voor welke stad wil je het weer opvragen? ")
    weather_data = get_weather_data(city_name, API_key)
    
    vraag = input("Welke informatie wil je zien? (temperatuur, windsnelheid, luchtvochtigheid) ")
    
    if vraag.lower() == "temperatuur":
        print(f"De temperatuur in {city_name} is {get_temperature(weather_data):.2f}°C")
    elif vraag.lower() == "windsnelheid":
        print(f"De windsnelheid in {city_name} is {get_wind_speed(weather_data)} m/s")
    elif vraag.lower() == "luchtvochtigheid":
        print(f"De luchtvochtigheid in {city_name} is {get_humidity(weather_data)}%")
    else:
        print("Ongeldige keuze.")
    
    extra_vraag = input("Wil je extra details zoals zonsopkomst en zonsondergang? (ja/nee) ")
    if extra_vraag.lower() == "ja":
        print(f"Het weer in {city_name} wordt omschreven als: {get_weather_description(weather_data)}")
        print(f"De zonsopkomst in {city_name} is om {get_sunrise_time(weather_data)} UTC")
        print(f"De zonsondergang in {city_name} is om {get_sunset_time(weather_data)} UTC")
