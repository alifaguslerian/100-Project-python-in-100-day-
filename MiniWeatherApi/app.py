from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Data cuaca default untuk beberapa kota
weather_data = {
    "jakarta": {"temperature": 22, "condition": "Sunny"},
    "paris": {"temperature": 15, "condition": "Cloudy"},
    "dubai": {"temperature": 28, "condition": "Clear"},
    "london": {"temperature": 18, "condition": "Rainy"}
}

# Daftar kondisi cuaca untuk randomisasi
weather_conditions = ["Sunny", "Cloudy", "Rainy", "Stormy", "Foggy", "Snowy"]

@app.route('/')
def home():
    return jsonify({"Message": "Welcome to the weather API!"})

@app.route('/weather', methods=['GET'])
def get_all_weather():
    # Randomisasi setiap kota saat data diambil
    randomized_weather = {
        city: {
            "temperature": random.randint(10, 35),  # Suhu acak antara 10-35 derajat
            "condition": random.choice(weather_conditions)
        }
        for city in weather_data
    }
    return jsonify(randomized_weather)

@app.route('/weather/<city>', methods=['GET'])
def get_weather_by_city(city):
    city = city.lower()
    if city in weather_data:
        # Generate cuaca acak
        random_weather = {
            "temperature": random.randint(10, 35),
            "condition": random.choice(weather_conditions)
        }
        return jsonify({city: random_weather})
    
    return jsonify({"error": "City not found"}), 404

@app.route('/weather', methods=['POST'])
def add_city_weather():
    data = request.json
    city = data.get('city', '').lower()
    temperature = data.get('temperature')
    condition = data.get('condition')

    if not city or not temperature or not condition:
        return jsonify({'error': 'Missing city, temperature, or condition'}), 400
    
    weather_data[city] = {"temperature": temperature, "condition": condition}
    return jsonify({"message": f"Weather for {city} added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
