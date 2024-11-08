import json
import random
from datetime import datetime

# Example pollution data for different grid locations
data = [
    {"location": [12.9716, 77.5946], "pollution_level": random.randint(50, 300)},  # Random pollution values
    {"location": [12.2958, 76.6394], "pollution_level": random.randint(50, 300)},
    {"location": [12.9141, 74.8560], "pollution_level": random.randint(50, 300)}
]

# Saving data to a JSON file for simulation purposes
with open("example_data.json", "w") as file:
    json.dump(data, file)

print("Data generated and saved to example_data.json")
