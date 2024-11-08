
# Real-Time Pollution Monitoring and Alerting System

## Overview
This project is a real-time web application that monitors pollution levels in different areas of a city and provides health alerts. It offers an interactive heatmap and notifications when pollution levels exceed safe thresholds. The application also suggests the safest route with minimal exposure to pollution for travel.

## Features
- **Real-Time Pollution Monitoring:** Displays the pollution levels in various city grids on a map.
- **Health Alerts:** Sends notifications when pollution exceeds safe levels.
- **Route Suggestion:** Calculates and displays the least polluted route based on current data.
- **Interactive Heatmap:** Visualizes pollution levels on a map for better decision-making.

## Data Structures and Algorithms
- **Grid (2D Array):** Represents city areas divided into grids, with each cell containing pollution data.
- **Dijkstra's Algorithm:** Used to find the route with the least exposure to pollution.
- **Hash Map:** Caches real-time data for quick access to pollution levels for each grid.
- **Time-Series Forecasting Models:** Predicts future pollution levels based on historical data.

## Requirements
- Python 3.x
- Flask
- Geopy
- Leaflet.js (for interactive maps)
- Other dependencies (listed in `requirements.txt`)

## Installation Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/hanushrajputh/Real-Time_Pollution_Monitoring.git
   cd Real-Time_Pollution_Monitoring
   ```

2. **Set Up a Virtual Environment:**

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Generate Example Data:**

   Run the `data_ingestion.py` script to generate initial pollution data in `example_data.json`:

   ```bash
   python data_ingestion.py
   ```

5. **Start the Flask Application:**

   ```bash
   python main.py
   ```

6. **Access the Application:**
   Open your browser and navigate to:

   ```
   http://127.0.0.1:5000/
   ```

   You should see the real-time pollution monitoring map.

## Project Structure
```
Real-Time_Pollution_Monitoring/
├── data_ingestion.py           # Script to generate example pollution data
├── env                         # Virtual environment folder
├── example_data.json           # Example pollution data
├── LICENSE                     # Project license
├── main.py                     # Main Flask app
├── README.md                   # Project documentation
├── requirements.txt            # List of required Python dependencies
├── routing.py                  # Route calculation logic
├── static/                     # Static files (e.g., CSS, JS)
│   ├── style.css               # Stylesheet
│   └── map.js                  # Map and data visualization logic
└── templates/                  # HTML templates
    └── heatmap.html            # Heatmap display page
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Leaflet.js for interactive maps
- Flask for web development
- Geopy for geospatial calculations

## Future Enhancements
- **Real-Time Pollution Data Integration:** Fetch live pollution data from APIs.
- **User Customization:** Allow users to set pollution thresholds and preferred routes.
- **Health Recommendations:** Provide health advice based on pollution levels.

## Contact
For any questions or feedback, feel free to reach out to [Your Name] at [Your Email].
