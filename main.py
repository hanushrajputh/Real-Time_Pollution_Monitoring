from flask import Flask, jsonify, render_template
import json
from geopy.distance import geodesic

app = Flask(__name__)

# Load pollution data
with open("example_data.json") as f:
    pollution_data = json.load(f)

# Endpoint to get pollution data
@app.route("/pollution_data")
def get_pollution_data():
    return jsonify(pollution_data)

# Endpoint to calculate the least polluted route (simple illustration)
@app.route("/route")
def calculate_route():
    # Assuming a mock route calculation based on lowest pollution levels
    sorted_data = sorted(pollution_data, key=lambda x: x["pollution_level"])
    return jsonify({"route": sorted_data})

if __name__ == "__main__":
    app.run(debug=True)
