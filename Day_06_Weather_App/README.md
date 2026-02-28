# Day 06 - Weather App

## Project Description

This is a professional Python-based weather application that fetches real-time weather data for specified cities using the Open-Meteo API. It provides current temperature, wind speed, and weather conditions.

## Features

*   **Real-time Weather Data**: Fetches current weather information from the Open-Meteo API.
*   **Supports Key Cities**: Provides weather data for a predefined list of major cities (London, New York, Tokyo, Sydney, Paris).
*   **User-friendly Interface**: Simple command-line interface for entering city names.
*   **Error Handling**: Includes basic error handling for API request failures and invalid city inputs.

## How to Run

1.  **Navigate to the project directory**:

    ```bash
    cd Day_06_Weather_App
    ```

2.  **Install the required library**:

    ```bash
    pip install requests
    ```

3.  **Run the weather application**:

    ```bash
    python weather_app.py
    ```

## Usage

Upon running the script, you will be prompted to enter a city name. The application will then display the current weather conditions for that city.

### Example Workflow

1.  **Enter city name**: `London`

    ```
    Weather in London:
      Temperature: 10.5°C
      Windspeed: 15.3 km/h
      Conditions: Partly cloudy
    ```

2.  **Enter another city name**: `New York`

    ```
    Weather in New York:
      Temperature: 5.2°C
      Windspeed: 20.1 km/h
      Conditions: Clear sky
    ```

3.  **Exit the application**: `exit`

    ```
    Enter city name (or 'exit' to quit): exit
    ```
