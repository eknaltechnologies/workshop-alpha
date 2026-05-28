# updated Day7

import json
from flask import Flask, request, jsonify, render_template

FILENAME = "unit_converter.json"
app = Flask(__name__)


def save_data(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)


def load_data():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"history": {}}


def add_history(data, original, converted):
    data["history"][original] = converted
    save_data(data)


@app.route("/")
def home():
    return "Welcome to the Unit Converter API!"


# ---------- FRONTEND ROUTES ----------
@app.route("/frontend")
def frontend():
    return render_template("index.html")

@app.route("/frontend/history")
def frontend_history():
    data = load_data()
    return render_template("history.html", history=data["history"])
# ------------------------------------


@app.route("/convert/km_to_m", methods=["POST"])
def km_to_m():
    km = float(request.json["value"])
    result = km * 1000
    data = load_data()
    add_history(data, f"{km} KM", f"{result} M")
    return jsonify({"converted_value": result, "unit": "M"})


@app.route("/convert/m_to_km", methods=["POST"])
def m_to_km():
    meters = float(request.json["value"])
    result = meters / 1000
    data = load_data()
    add_history(data, f"{meters} M", f"{result} KM")
    return jsonify({"converted_value": result, "unit": "KM"})


@app.route("/convert/kg_to_g", methods=["POST"])
def kg_to_g():
    kg = float(request.json["value"])
    result = kg * 1000
    data = load_data()
    add_history(data, f"{kg} KG", f"{result} G")
    return jsonify({"converted_value": result, "unit": "G"})


@app.route("/convert/g_to_kg", methods=["POST"])
def g_to_kg():
    grams = float(request.json["value"])
    result = grams / 1000
    data = load_data()
    add_history(data, f"{grams} G", f"{result} KG")
    return jsonify({"converted_value": result, "unit": "KG"})


@app.route("/convert/in_to_cm", methods=["POST"])
def in_to_cm():
    inches = float(request.json["value"])
    cm = inches * 2.54
    data = load_data()
    add_history(data, f"{inches} IN", f"{cm} CM")
    return jsonify({"converted_value": cm, "unit": "CM"})


@app.route("/convert/cm_to_in", methods=["POST"])
def cm_to_in():
    cm = float(request.json["value"])
    inches = cm / 2.54
    data = load_data()
    add_history(data, f"{cm} CM", f"{inches} IN")
    return jsonify({"converted_value": inches, "unit": "IN"})


@app.route("/history", methods=["GET"])
def view_history():
    data = load_data()
    return jsonify(data["history"])


@app.route("/history/delete", methods=["POST"])
def delete_history():
    key = request.json["key"]
    data = load_data()
    if key in data["history"]:
        del data["history"][key]
        save_data(data)
        return jsonify({"message": "History deleted successfully."})
    else:
        return jsonify({"message": "Conversion record not found."})


@app.route("/total", methods=["GET"])
def total_conversions():
    data = load_data()
    return jsonify({"total_conversions": len(data["history"])})


if __name__ == "__main__":
    app.run(debug=True)
