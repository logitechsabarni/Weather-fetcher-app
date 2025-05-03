import requests

def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data.get("cod") != 200:
            print(f"❌ Error: {data.get('message', 'City not found.')}")
            return

        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        print(f"\n🌍 Weather in {city.capitalize()}:")
        print(f"🌡️ Temperature: {temp}°C (Feels like {feels_like}°C)")
        print(f"☁️ Description: {weather.capitalize()}")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌬️ Wind Speed: {wind} m/s")

    except requests.exceptions.RequestException as e:
        print("⚠️ Network error:", e)

if __name__ == "__main__":
    print("=== Weather Fetcher CLI ===")
    api_key = "YOUR_API_KEY_HERE"  # 🔐 Replace with your OpenWeatherMap API key
    city = input("Enter city name: ").strip()
    if city:
        get_weather(city, api_key)
    else:
        print("❗ City name cannot be empty.")
