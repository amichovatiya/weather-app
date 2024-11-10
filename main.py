from flask import Flask, render_template, request, redirect, url_for
from services.openai_service import extract_city_from_text
from services.weather_service import get_weather_data, get_forecast_data
import string
import datetime
from query_data import query_rag

app = Flask(__name__)

# Dummy function to simulate credential checking
def check_credentials(password):
    
    if not password:
        return False
    
    try:
        return query_rag(password) == "True"
    except FileNotFoundError:
        print(f"Error with RAG credentials check: {e}")
        return False

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form.get("search")
        password = request.form.get("password")

        city_or_message = extract_city_from_text(user_input)
        
        if "Oops!" in city_or_message:
            return render_template("error.html", error_message=city_or_message)
        
        # If credentials are provided, check them
        is_valid_credentials = check_credentials(password)

        # Pass the validation result to the next route
        return redirect(url_for("get_weather", city=city_or_message, valid_credentials=is_valid_credentials))
    
    return render_template("index.html")

@app.route("/<city>", methods=["GET", "POST"])
def get_weather(city):
    city_name = string.capwords(city)
    current_date = datetime.datetime.now().strftime("%A, %B %d")

    # Fetch weather data
    today_weather = get_weather_data(city_name)
    forecast_summary = get_forecast_data(city_name) or []  # Ensures forecast_summary is an iterable list
    
    valid_credentials = request.args.get("valid_credentials", default="false").lower() == "true"

    # Render the city weather template with today's weather and forecast summary
    return render_template(
        "city.html",
        city_name=city_name,
        current_date=current_date,
        today_weather=today_weather,
        forecast_summary=forecast_summary,
        valid_credentials=valid_credentials
    )

@app.route("/error")
def error():
    return render_template("error.html")

if __name__ == "__main__":
    app.run(debug=True)
