from flask import Flask, render_template, request, redirect, url_for
from services.openai_service import extract_city_from_text
from services.weather_service import get_weather_data, get_forecast_data
import string
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form.get("search")
        city_or_message = extract_city_from_text(user_input)
        if "Oops!" in city_or_message:
            return render_template("error.html", error_message=city_or_message)
        else:
            return redirect(url_for("get_weather", city=city_or_message))
    return render_template("index.html")

@app.route("/<city>", methods=["GET", "POST"])
def get_weather(city):
    city_name = string.capwords(city)
    current_date = datetime.datetime.now().strftime("%A, %B %d")

    # Fetch weather data
    today_weather = get_weather_data(city_name)
    forecast_summary = get_forecast_data(city_name) or []  # Ensures forecast_summary is an iterable list

    # Render the city weather template with today's weather and forecast summary
    return render_template(
        "city.html",
        city_name=city_name,
        current_date=current_date,
        today_weather=today_weather,
        forecast_summary=forecast_summary
    )

@app.route("/error")
def error():
    return render_template("error.html")

if __name__ == "__main__":
    app.run(debug=True)
