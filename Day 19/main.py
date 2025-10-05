import requests

# API SETUP
API_KEY = "20b719619384000dc4fb75e5073d73b0"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Get weather data
def get_weather_data(city):
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"  # Perbaiki URL
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                "city": data["name"],
                "temperature": f"{data['main']['temp']}°C",
                "weather": data["weather"][0]["description"].title(),
                "humidity": f"{data['main']['humidity']}%",
                "wind_speed": f"{data['wind']['speed']} m/s",
            }
            return weather
        elif response.status_code == 404:
            print("City not found")
        else:
            print("An error occurred. Status Code: ", response.status_code)
    except Exception as e:
        print(f"An error occurred: ", e)
    return None  # Perbaiki penulisan None

# Display weather data
def display_weather_data(weather):
    if weather:  # Pastikan weather ada sebelum menampilkan
        print(f"City: {weather['city']}")
        for key, value in weather.items():
            if key != 'city':  # Jangan tampilkan 'city' lagi
                print(f"{key.title()}: {value}")

# Main program
while True:
    print("\n--- Weather App ---")
    city = input("Masukkan nama kota (atau ketik 'exit' untuk keluar): ").strip()
    if city.lower() == "exit":
        print("Keluar dari program. Sampai jumpa!")
        break
    weather = get_weather_data(city)
    display_weather_data(weather)
