import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OWM_API_KEY = os.getenv("OWM_API_KEY")
    OWM_CURRENT_WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
    OWM_FORECAST_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
    GEOCODING_API_ENDPOINT = "http://api.openweathermap.org/geo/1.0/direct"
