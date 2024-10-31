import requests
from config import Config

def get_weather_data(city_name):
    # Get latitude and longitude for city
    location_params = {
        "q": city_name,
        "appid": Config.OWM_API_KEY,
        "limit": 1,
    }
    location_response = requests.get(Config.GEOCODING_API_ENDPOINT, params=location_params)
    location_data = location_response.json()
    if not location_data:
        return None
    
    lat = location_data[0]['lat']
    lon = location_data[0]['lon']

    # Get current weather data
    current_weather_params = {
        "lat": lat,
        "lon": lon,
        "appid": Config.OWM_API_KEY,
        "units": "metric",
    }
    response = requests.get(Config.OWM_CURRENT_WEATHER_ENDPOINT, params=current_weather_params)
    data = response.json()
    return {
        "temp": round(data['main']['temp']),
        "temp_min": round(data['main']['temp_min']),
        "temp_max": round(data['main']['temp_max']),
        "wind_speed": round(data['wind']['speed'], 1),
        "humidity": round(data['main']['humidity']),
        "weather": data['weather'][0]['main']
    }

def get_forecast_data(city_name):
    # Get latitude and longitude for city
    location_params = {
        "q": city_name,
        "appid": Config.OWM_API_KEY,
        "limit": 1,
    }
    location_response = requests.get(Config.GEOCODING_API_ENDPOINT, params=location_params)
    location_data = location_response.json()
    if not location_data:
        return []

    lat = location_data[0]['lat']
    lon = location_data[0]['lon']

    # Get forecast data
    forecast_params = {
        "lat": lat,
        "lon": lon,
        "appid": Config.OWM_API_KEY,
        "units": "metric",
    }
    response = requests.get(Config.OWM_FORECAST_ENDPOINT, params=forecast_params)
    if response.status_code != 200:
        # Log error if the response is unsuccessful
        print(f"Error: Received status code {response.status_code} from forecast API")
        return []

    forecast_data = response.json()

    if 'list' not in forecast_data:
        print("Error: 'list' key not in forecast_data JSON")
        return []

    # Process forecast data into daily summaries
    daily_forecast = {}
    for item in forecast_data['list']:
        date_str = item['dt_txt'].split(" ")[0]
        if date_str not in daily_forecast:
            daily_forecast[date_str] = {
                "temp_min": float('inf'),
                "temp_max": float('-inf'),
                "wind_speed_total": 0,
                "wind_count": 0,
                "humidity_total": 0,
                "humidity_count": 0,
                "rain": 0,
                "weather": item['weather'][0]['main'],
                "data_points": 0
            }
        
        daily_forecast[date_str]["temp_min"] = min(daily_forecast[date_str]["temp_min"], item['main']['temp_min'])
        daily_forecast[date_str]["temp_max"] = max(daily_forecast[date_str]["temp_max"], item['main']['temp_max'])
        
        daily_forecast[date_str]["wind_speed_total"] += item['wind']['speed']
        daily_forecast[date_str]["wind_count"] += 1
        daily_forecast[date_str]["humidity_total"] += item['main']['humidity']
        daily_forecast[date_str]["humidity_count"] += 1
        
        if 'rain' in item and '3h' in item['rain']:
            daily_forecast[date_str]["rain"] += item['rain']['3h']
        
        daily_forecast[date_str]["data_points"] += 1

    forecast_summary = []
    for date, data in daily_forecast.items():
        average_wind_speed = data["wind_speed_total"] / data["wind_count"]
        average_humidity = data["humidity_total"] / data["humidity_count"]
        
        forecast_summary.append({
            "date": date,
            "temp_min": round(data["temp_min"]),
            "temp_max": round(data["temp_max"]),
            "wind_speed": round(average_wind_speed, 1),
            "rain": round(data["rain"], 2),
            "humidity": round(average_humidity),
            "weather": data["weather"]
        })

    return forecast_summary    # Get latitude and longitude for city
    location_params = {
        "q": city_name,
        "appid": Config.OWM_API_KEY,
        "limit": 1,
    }
    location_response = requests.get(Config.GEOCODING_API_ENDPOINT, params=location_params)
    location_data = location_response.json()
    if not location_data:
        return None
    
    lat = location_data[0]['lat']
    lon = location_data[0]['lon']

    # Get forecast data
    forecast_params = {
        "lat": lat,
        "lon": lon,
        "appid": Config.OWM_API_KEY,
        "units": "metric",
    }
    response = requests.get(Config.OWM_FORECAST_ENDPOINT, params=forecast_params)
    forecast_data = response.json()

    # Process forecast data into daily summaries
    daily_forecast = {}
    for item in forecast_data['list']:
        date_str = item['dt_txt'].split(" ")[0]
        if date_str not in daily_forecast:
            daily_forecast[date_str] = {
                "temp_min": float('inf'),
                "temp_max": float('-inf'),
                "wind_speed_total": 0,
                "wind_count": 0,
                "humidity_total": 0,
                "humidity_count": 0,
                "rain": 0,
                "weather": item['weather'][0]['main'],
                "data_points": 0
            }
        
        daily_forecast[date_str]["temp_min"] = min(daily_forecast[date_str]["temp_min"], item['main']['temp_min'])
        daily_forecast[date_str]["temp_max"] = max(daily_forecast[date_str]["temp_max"], item['main']['temp_max'])
        
        daily_forecast[date_str]["wind_speed_total"] += item['wind']['speed']
        daily_forecast[date_str]["wind_count"] += 1
        daily_forecast[date_str]["humidity_total"] += item['main']['humidity']
        daily_forecast[date_str]["humidity_count"] += 1
        
        if 'rain' in item and '3h' in item['rain']:
            daily_forecast[date_str]["rain"] += item['rain']['3h']
        
        daily_forecast[date_str]["data_points"] += 1

    forecast_summary = []
    for date, data in daily_forecast.items():
        average_wind_speed = data["wind_speed_total"] / data["wind_count"]
        average_humidity = data["humidity_total"] / data["humidity_count"]
        
        forecast_summary.append({
            "date": date,
            "temp_min": round(data["temp_min"]),
            "temp_max": round(data["temp_max"]),
            "wind_speed": round(average_wind_speed, 1),
            "rain": round(data["rain"], 2),
            "humidity": round(average_humidity),
            "weather": data["weather"]
        })

    return forecast_summary
