import urllib.request
import json


def get_coordinates(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
    if "results" not in data or not data["results"]:
        return None
    result = data["results"][0]
    return {
        "name": result["name"],
        "country": result.get("country", ""),
        "latitude": result["latitude"],
        "longitude": result["longitude"]
    }


def get_weather(latitude, longitude):
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}"
        f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weathercode"
        f"&daily=temperature_2m_max,temperature_2m_min,precipitation_sum"
        f"&timezone=auto&forecast_days=5"
    )
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode())


def weather_description(code):
    descriptions = {
        0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
        45: "Foggy", 48: "Icy fog", 51: "Light drizzle", 53: "Drizzle",
        55: "Heavy drizzle", 61: "Light rain", 63: "Rain", 65: "Heavy rain",
        71: "Light snow", 73: "Snow", 75: "Heavy snow", 80: "Rain showers",
        81: "Heavy rain showers", 82: "Violent rain showers",
        95: "Thunderstorm", 96: "Thunderstorm with hail"
    }
    return descriptions.get(code, "Unknown")


def show_weather():
    print("=" * 50)
    print("            WEATHER APP")
    print("=" * 50)

    city = input("\nEnter city name: ").strip()
    if not city:
        print("City name cannot be empty.")
        return

    print(f"\nFetching weather for {city}...")

    try:
        location = get_coordinates(city)
        if not location:
            print(f"Could not find city: {city}")
            return

        weather = get_weather(location["latitude"], location["longitude"])
        current = weather["current"]
        daily = weather["daily"]

        print("\n" + "=" * 50)
        print(f"  {location['name']}, {location['country']}")
        print("=" * 50)
        print(f"  Condition:   {weather_description(current['weathercode'])}")
        print(f"  Temperature: {current['temperature_2m']}°C")
        print(f"  Humidity:    {current['relative_humidity_2m']}%")
        print(f"  Wind Speed:  {current['wind_speed_10m']} km/h")

        print("\n  5-DAY FORECAST:")
        print("  " + "-" * 44)
        for i in range(5):
            date = daily["time"][i]
            high = daily["temperature_2m_max"][i]
            low = daily["temperature_2m_min"][i]
            rain = daily["precipitation_sum"][i]
            print(f"  {date}  High: {high}°C  Low: {low}°C  Rain: {rain}mm")

        print("=" * 50)

    except Exception as e:
        print(f"Error fetching weather: {e}")


def main():
    while True:
        show_weather()
        again = input("\nCheck another city? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
