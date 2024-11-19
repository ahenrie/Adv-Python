from flask import render_template, request, redirect, url_for
from app import db
from app.models import WeatherData

def index():
    """
    Root route that displays a form to select a location for weather data.
    If a POST request is made with a location selected, redirects to
    the weather_data route with the selected location as a query parameter.

    Returns:
        - Renders the 'index.html' template with a list of unique locations
          fetched from the database for use in the dropdown menu.
    """
    if request.method == "POST":
        location = request.form.get("location")
        return redirect(url_for("weather_data", location=location))

    locations = db.session.query(WeatherData.location).distinct().all()
    return render_template("index.html", locations=[loc[0] for loc in locations])

def weather_data():
    """
    Route that displays weather data for a selected location.
    If a location query parameter is provided, filters the data by that location;
    otherwise, displays all weather data.

    Returns:
        - Renders the 'weather.html' template with weather records matching the
          specified location, or all records if no location is specified.
    """
    location = request.args.get("location")
    if location:
        records = WeatherData.query.filter_by(location=location).all()
    else:
        records = WeatherData.query.all()
    return render_template("weather.html", records=records)
