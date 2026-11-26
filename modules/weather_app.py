import requests

API_KEY = "a23babea3c4dd5a64e81fba2c11ea1bd"

def start():
    print("\n========== WEATHER APP ==========")

    city = input("Enter your city name: ")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()




    if response.status_code == 200:
        print("\nCity:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Weather:", data["weather"][0]["description"])
        print("Humidity:", data["main"]["humidity"], "%")
        print("Wind Speed:", data["wind"]["speed"], "m/s")
    else:
        print("City not found!")