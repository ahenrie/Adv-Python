import pandas as pd
import numpy as np
import pickle

# Load the trained model
with open('app/rainfall_predictor_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define categorical variables and their possible values
locations = ['Sydney', 'Melbourne', 'Brisbane', 'Adelaide', 'Perth']
wind_dirs = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW', 'Calm']
rain_today_options = ['Yes', 'No']

# Function to generate dummy data
def generate_dummy_data(num_samples=10):
    dummy_data = {
        'MinTemp': np.random.uniform(-5, 40, num_samples),  # Temperatures between -5°C and 40°C
        'MaxTemp': np.random.uniform(0, 45, num_samples),  # Temperatures between 0°C and 45°C
        'Rainfall': np.random.uniform(0, 50, num_samples),  # Rainfall between 0mm and 50mm
        'Humidity9am': np.random.uniform(20, 100, num_samples),  # Humidity between 20% and 100%
        'Humidity3pm': np.random.uniform(20, 100, num_samples),  # Humidity between 20% and 100%
        'Pressure9am': np.random.uniform(1000, 1035, num_samples),  # Pressure between 1000hPa and 1035hPa
        'Pressure3pm': np.random.uniform(1000, 1035, num_samples),  # Pressure between 1000hPa and 1035hPa
        'Location': np.random.choice(locations, num_samples),  # Randomly select locations
        'WindGustDir': np.random.choice(wind_dirs, num_samples),  # Randomly select wind gust directions
        'WindDir9am': np.random.choice(wind_dirs, num_samples),  # Randomly select wind directions at 9am
        'WindDir3pm': np.random.choice(wind_dirs, num_samples),  # Randomly select wind directions at 3pm
        'RainToday': np.random.choice(rain_today_options, num_samples)  # Randomly select Yes/No for rain today
    }
    return pd.DataFrame(dummy_data)

# Generate dummy data
dummy_data = generate_dummy_data(100000)

# Preprocess dummy data for prediction
dummy_data['RainToday'] = dummy_data['RainToday'].map({'Yes': 1, 'No': 0})  # Encode RainToday as 1/0
dummy_data = pd.get_dummies(dummy_data, columns=['Location', 'WindGustDir', 'WindDir9am', 'WindDir3pm'], drop_first=True)

# Ensure dummy data has all necessary columns for the model
for feature in model.feature_names_in_:
    if feature not in dummy_data.columns:
        dummy_data[feature] = 0

# Drop any extra columns not seen during training
dummy_data = dummy_data[model.feature_names_in_]

# Predict rainfall using the model
predictions = model.predict(dummy_data)

# Add predictions to the dummy data for inspection
dummy_data['PredictedRainfall'] = predictions

# Display results
print(dummy_data[['MinTemp', 'MaxTemp', 'Rainfall', 'Humidity9am', 'Humidity3pm',
                  'Pressure9am', 'Pressure3pm', 'PredictedRainfall']])
