import requests

API_KEY = "8d601d547d2d435518b8ada71f582209"
URL = "https://api.openweathermap.org/data/2.5/weather"
city = input("Please enter a city name: ")

api_call = f"{URL}?appid={API_KEY}&q={city}&units=metric"
response = requests.get(api_call)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['main']
    temperature = round(data['main']['temp'])
    wind = round(data['wind']['speed'])
    print("The current weather in", city, "is", weather, "with a the temperature of", temperature, "Celsius, and a windspeed of", wind, "miles per hour.")
else:
    print("error")

