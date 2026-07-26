#mission 23 weather api taaki kahi ka bhi weather jaan sake through jarvis by saying example weather in nashik or dhule

#importing
import os
import requests

from dotenv import load_dotenv

#.env loading
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")


#FUNCTION DEFINING
def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    if data["cod"] != 200:
        return None

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]
    city_name = data["name"]

    return city_name, temperature, humidity, weather