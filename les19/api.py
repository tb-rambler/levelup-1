import requests
import logging

logging.basicConfig(
    filename="lesson_19/weather.log", 
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 55.7558,
    "longitude": 37.6173,
    'current_weather': True
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print("Температура сейчас:", data['current_weather']["temperature"], "C")
    logging.info(f"{data['current_weather']["temperature"]} C")
else:
    print("Ошибка: ", response.status_code)
    logging.error(f"Error - {response.status_code}")
    