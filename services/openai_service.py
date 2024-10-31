import openai
import re
from config import Config

openai.api_key = Config.OPENAI_API_KEY

def extract_city_from_text(user_text):
    messages = [
        {"role": "system", "content": "You are a helpful assistant that extracts city names from user queries and try to relate it the city thats makes most sense according to it. You have to answer just the city name. No extra text. Make sure its a CITY and not a country"},
        {"role": "user", "content": f"The user asked: '{user_text}'. Please think and extract the city name for this query."}
    ]
    
    # Call the ChatCompletion API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=10
    )
    city_name = response['choices'][0]['message']['content'].strip()
    if re.match(r"^[A-Za-z\s\-]+$", city_name):
        return city_name
    else:
        return f"Oops! Couldn't find the city. Got: '{city_name}'"