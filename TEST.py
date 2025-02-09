from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
EXTERNAL_API_URL = "https://api.le-systeme-solaire.net/rest/bodies/"
local_missions = []
@app.route('/planets', methods=['GET'])
def get_planets():
    try:
        response = requests.get(EXTERNAL_API_URL)
        response.raise_for_status()  # Controleer op fouten
        bodies = response.json()["bodies"]
        planets = [body for body in bodies if body.get("isPlanet")]
        return jsonify(planets), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Er is een probleem opgetreden bij het ophalen van planeten.", "details": str(e)}), 500

@app.route('/planet/<name>', methods=['GET'])
def get_planet(name):
    try:
        response = requests.get(EXTERNAL_API_URL)
        response.raise_for_status()
        bodies = response.json()["bodies"]
        planet = next((body for body in bodies if body.get("englishName", "").lower() == name.lower()), None)
        if planet:
            return jsonify(planet), 200
        else:
            return jsonify({"error": f"Planeet '{name}' niet gevonden."}), 404
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Er is een probleem opgetreden bij het ophalen van de planeet.", "details": str(e)}), 500

@app.route('/add_mission', methods=['POST'])
def add_mission():
    try:
        new_mission = request.get_json()
        new_mission["id"] = len(local_missions) + 1  # Unieke ID voor missies
        local_missions.append(new_mission)
        return jsonify({"message": "Missie succesvol toegevoegd.", "mission": new_mission}), 201
    except Exception as e:
        return jsonify({"error": "Er is een probleem opgetreden bij het toevoegen van de missie.", "details": str(e)}), 400
if __name__ == '__main__':
    print("Welkom bij de Space Explorer API!")
    while True:
        print("\nKies een optie:")
        print("1. Planeten ophalen")
        print("2. Specifieke planeet zoeken")
        print("3. Ruimtemissie toevoegen")
        print("4. Stoppen")

        keuze = input("Voer je keuze in (1-4): ")

        if keuze == "1":
            print("Planeten ophalen...")
            response = requests.get("http://127.0.0.1:5000/planets")
            print(response.json())
        elif keuze == "2":
            naam = input("Voer de naam van de planeet in: ")
            response = requests.get(f"http://127.0.0.1:5000/planet/{naam}")
            print(response.json())
        elif keuze == "3":
            naam = input("Voer de naam van de missie in: ")
            bestemming = input("Voer de bestemming van de missie in: ")
            lanceerdatum = input("Voer de lanceerdatum in (YYYY-MM-DD): ")
            missie_data = {
                "name": naam,
                "destination": bestemming,
                "launch_date": lanceerdatum
            }
            response = requests.post("http://127.0.0.1:5000/add_mission", json=missie_data)
            print(response.json())
        elif keuze == "4":
            print("Programma wordt afgesloten. Tot ziens!")
            break
        else:
            print("Ongeldige keuze. Probeer opnieuw.")

    app.run(debug=True, use_reloader=False)
