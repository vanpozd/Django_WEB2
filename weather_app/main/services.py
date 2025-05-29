import requests
from django.conf import settings

def get_weather_for_city(city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': settings.OPENWEATHERMAP_API_KEY,
        'units': 'metric',
        'lang': 'ua',
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            'temperature': f"{data['main']['temp']} °C",
            'description': data['weather'][0]['description'],
            'humidity': f"{data['main']['humidity']}%",
            'wind': f"{data['wind']['speed']} м/с",
        }
    return None
