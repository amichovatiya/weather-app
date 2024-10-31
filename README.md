# 🌦️ Weather App with OpenAI City Extraction

This project is a weather application built with **Flask**. It integrates **OpenAI GPT-3.5** to extract city names from user input and fetches the weather forecast using **OpenWeatherMap's API**.

## ✨ Features

- **City Extraction with OpenAI**: Users can input queries in natural language (e.g., *"What's the weather like in New York?"*). The app uses GPT-3.5 to extract the city name from the query.
- **Current Weather & 5-day Forecast**: Displays the current weather (temperature, condition, wind speed) and a 5-day forecast for the selected city.
- **Error Handling**: Redirects to an error page if the city name is invalid or if weather data cannot be retrieved.

## 🛠️ Technologies

- **Backend**: Flask
- **APIs**: 
  - [OpenWeatherMap API](https://openweathermap.org/api) (for weather data and geocoding)
  - [OpenAI GPT-3.5](https://beta.openai.com/signup/) (for extracting city names from user input)
- **Frontend**: HTML, CSS
- **Libraries**:
  - `requests`: For making HTTP requests to APIs.
  - `dotenv`: For environment variable management.
  - `re`: For regex-based city name validation.

## 📋 Prerequisites

Before running this project, make sure you have:

- **Python**: Version 3.7 or higher.
- **API Keys**:
  - OpenWeatherMap API Key
  - OpenAI API Key

## 🚀 Installation

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app

### 2. Create and Activate a Virtual Environment

Create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: `venv\Scripts\activate`

### 3. Install Dependencies

Install all the required dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt


### 4. Set Up Environment Variables

Create a `.env` file in the root directory and add your API keys as shown below:

```plaintext
OWM_API_KEY=your_openweathermap_api_key
OPENAI_API_KEY=your_openai_api_key


### 5. Run the Application

Once you've set up the environment variables and installed the dependencies, you can start the Flask app:

```bash
flask run

## 🔧 Usage

1. Open your browser and visit `http://127.0.0.1:5000/`.
2. Enter a natural language query in the search bar, such as **"What's the weather like in Paris?"**.
3. The app will extract the city name using GPT-3.5 and display the weather data for that city.

### Example Queries

- *"What’s the weather like in Paris?"*
- *"Show me the weather forecast for New York."*
- *"Tell me the weather in Tokyo."*

## 🗂️ Project Structure

```plaintext
.
├── app.py                   # Main application file
├── requirements.txt          # Dependencies for the project
├── templates/                # HTML templates
│   ├── index.html            # Main page with search input
│   ├── city.html             # Weather display page
│   └── error.html            # Error page template
├── static/                   # Static files (CSS, JS, images)
├── .env                      # Environment variables (API keys)
└── README.md                 # This file

## ⚠️ Error Handling

If the city name is invalid or weather data can't be retrieved, the app will redirect to an error page showing a message like:

- *"Oops! Looks like I couldn't find the city you are looking for. Try asking again!"*
  
The error page provides a user-friendly explanation and encourages users to try entering a different query or city.

## 📝 License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this software as per the terms of the license.

---

## 🔄 Future Improvements

Here are a few potential enhancements to the project:

- **Improved City Recognition**: Fine-tune city extraction for ambiguous user queries or spelling mistakes.
- **Weather Alerts**: Include severe weather alerts, if any, for the city.
- **Historical Weather Data**: Allow users to check past weather data for specific dates.
- **User Authentication**: Add a login system to save user preferences and favorite cities.

---

Feel free to fork and modify the project or contribute improvements via pull requests!

# weather-app
# weather-app
# CYSE-690---Error-401s
