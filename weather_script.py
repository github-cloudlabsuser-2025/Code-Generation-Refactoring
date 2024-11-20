import requests

def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def main():
    api_key = "514ec865e90de2a835c7d8a0a53ec43b"
    city = input("Introduce el nombre de la ciudad: ")
    weather_data = get_weather(city, api_key)
    if weather_data:
        print(f"Clima en {city}:")
        print(f"Temperatura: {weather_data['main']['temp']}°C")
        print(f"Descripción: {weather_data['weather'][0]['description']}")
    else:
        print("No se pudo obtener el clima. Verifica el nombre de la ciudad y tu API Key.")

if __name__ == "__main__":
    main()