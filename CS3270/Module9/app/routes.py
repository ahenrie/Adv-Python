from app.extensions import db
from flask import render_template, request, redirect, url_for
from app.models import WeatherData
import pickle
import numpy as np

# Load the trained model
with open('app/rainfall_predictor_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

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

import pandas as pd

'''
def predict():
    """
    Route for making rainfall predictions.
    """
    # Fetch options for dropdowns
    locations = db.session.query(WeatherData.location).distinct().all()
    wind_dirs = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW', 'Calm']  # example directions
    rain_options = ['Yes', 'No']  # Yes or No for rain today

    if request.method == "POST":
        # Extract input values from the form
        input_data = {
            'Location': request.form['Location'],
            'WindGustDir': request.form['WindGustDir'],
            'WindDir9am': request.form['WindDir9am'],
            'WindDir3pm': request.form['WindDir3pm'],
            'RainToday': request.form['RainToday'],
            'MinTemp': request.form['MinTemp'],
            'MaxTemp': request.form['MaxTemp'],
            'Rainfall': request.form['Rainfall'],
        }

        # Preprocess categorical variables
        input_data['RainToday'] = 1 if input_data['RainToday'].lower() == 'yes' else 0

        # Convert to a DataFrame with the same columns as the model
        feature_vector = []
        for feature in model.feature_names_in_:
            if feature in input_data:
                value = input_data[feature]
                # Handle categorical features (you could use one-hot encoding here if needed)
                if isinstance(value, str) and value.isnumeric():
                    feature_vector.append(float(value))
                else:
                    feature_vector.append(0)
            else:
                feature_vector.append(0)

        # Convert to DataFrame for proper feature names
        feature_vector_df = pd.DataFrame([feature_vector], columns=model.feature_names_in_)

        # Make prediction
        prediction = model.predict(feature_vector_df)[0]

        return render_template('predict.html', prediction=round(prediction, 2),
                               locations=locations, wind_dirs=wind_dirs, rain_options=rain_options)

    # For GET request, render the form with dropdowns
    return render_template('predict.html', prediction=None,
                           locations=locations, wind_dirs=wind_dirs, rain_options=rain_options)

    print("Feature vector:", feature_vector)
'''

def predict():
    """
    Route to predict rainfall amount based on user inputs.
    """
    # Fetch dropdown options
    locations = [row[0] for row in db.session.query(WeatherData.location).distinct()]
    wind_dirs = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW', 'Calm']  # example directions
    rain_options = ['Yes', 'No']  # Yes or No for Rain Today

    if request.method == 'POST':
        # Get user inputs from the form
        user_input = {
            'Location': request.form['Location'],
            'WindGustDir': request.form['WindGustDir'],
            'WindDir9am': request.form['WindDir9am'],
            'WindDir3pm': request.form['WindDir3pm'],
            'RainToday': 1 if request.form['RainToday'] == 'Yes' else 0,
            'MinTemp': float(request.form['MinTemp']),
            'MaxTemp': float(request.form['MaxTemp']),
            'Rainfall': float(request.form['Rainfall']),
            'Humidity9am': float(request.form['Humidity9am']),
            'Humidity3pm': float(request.form['Humidity3pm']),
            'Pressure9am': float(request.form['Pressure9am']),
            'Pressure3pm': float(request.form['Pressure3pm']),
        }

        # Process inputs: Ensure the input DataFrame matches model's training columns
        input_df = pd.DataFrame([user_input])

        # Handle categorical variables (use one-hot encoding if required)
        input_df = pd.get_dummies(input_df)
        input_df = input_df.reindex(columns=model.feature_names_in_, fill_value=0)

        # Make prediction
        prediction = model.predict(input_df)[0]

        return render_template(
            'predict.html',
            prediction=round(prediction, 2),
            locations=locations,
            wind_dirs=wind_dirs,
            rain_options=rain_options
        )

    # For GET request, render the form
    return render_template('predict.html', prediction=None, locations=locations, wind_dirs=wind_dirs, rain_options=rain_options)
