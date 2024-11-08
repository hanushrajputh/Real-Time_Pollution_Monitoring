# Real-Time Pollution Monitoring and Alerting System

This is a real-time web application to monitor pollution levels in various areas of a city, providing interactive heatmaps, health alerts, and route suggestions for minimal pollution exposure.

## Features
- **Pollution Heatmap:** Displays pollution levels on a map.
- **Health Alerts:** Notifies users when pollution exceeds safe limits.
- **Safe Route Suggestions:** Recommends routes with the least pollution.

## Installation
1. Clone the repository.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run `data_ingestion.py` to generate example pollution data.
4. Start the application:
   ```
   python main.py
   ```

Access the application at `http://127.0.0.1:5000/`.

## Technologies
- Python (Flask)
- JavaScript (Leaflet)
- HTML/CSS (Interactive UI)

## Example Data
Sample data is provided in `example_data.json` for testing purposes.
