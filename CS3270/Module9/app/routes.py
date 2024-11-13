from flask import Blueprint, render_template
from app.models import WeatherData

main = Blueprint('main', __name__)

@main.route('/')
def index():
    weather_records = WeatherData.query.all()
    return render_template('weather.html', records=weather_records)
