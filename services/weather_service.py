import requests
from config import Config

def get_weather_data(city_name):
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

    current_weather_params = {
        "lat": lat,
        "lon": lon,
        "appid": Config.OWM_API_KEY,
        "units": "metric",
    }
    response = requests.get(Config.OWM_CURRENT_WEATHER_ENDPOINT, params=current_weather_params)
    data = response.json()
    result = {
        "temp": round(data['main']['temp']),
        "temp_min": round(data['main']['temp_min']),
        "temp_max": round(data['main']['temp_max']),
        "wind_speed": round(data['wind']['speed'], 1),
        "humidity": round(data['main']['humidity']),
        "weather": data['weather'][0]['main']
    }
    print("Current weather data:", result)  # Debugging print statement
    return result

def get_forecast_data(city_name):
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

    forecast_params = {
        "lat": lat,
        "lon": lon,
        "appid": Config.OWM_API_KEY,
        "units": "metric",
    }
    response = requests.get(Config.OWM_FORECAST_ENDPOINT, params=forecast_params)
    forecast_data = response.json()

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
            }
        
        daily_forecast[date_str]["temp_min"] = min(daily_forecast[date_str]["temp_min"], item['main']['temp_min'])
        daily_forecast[date_str]["temp_max"] = max(daily_forecast[date_str]["temp_max"], item['main']['temp_max'])
        daily_forecast[date_str]["wind_speed_total"] += item['wind']['speed']
        daily_forecast[date_str]["wind_count"] += 1
        daily_forecast[date_str]["humidity_total"] += item['main']['humidity']
        daily_forecast[date_str]["humidity_count"] += 1
        if 'rain' in item and '3h' in item['rain']:
            daily_forecast[date_str]["rain"] += item['rain']['3h']

    forecast_summary = []
    for date, values in daily_forecast.items():
        forecast_summary.append({
            "date": date,
            "temp_min": round(values["temp_min"]),
            "temp_max": round(values["temp_max"]),
            "wind_speed": round(values["wind_speed_total"] / values["wind_count"], 1),
            "humidity": round(values["humidity_total"] / values["humidity_count"]),
            "rain": round(values["rain"], 1),
            "weather": values["weather"],
        })
    return forecast_summary
