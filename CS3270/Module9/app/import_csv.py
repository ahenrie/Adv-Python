import csv
from app import db
from app.models import WeatherData
from app import create_app

# Initialize your Flask app context
app = create_app()
app.app_context().push()

with app.app_context():
    db.create_all()

# Define the path CSV
csv_file_path = './data/Weather Test Data.csv'

# Open the CSV file and read data
with open(csv_file_path, newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)  # Use DictReader for labeled columns

    for row in csv_reader:
        # Create a new WeatherData instance for each row in the CSV, with null-handling for optional fields
        weather_entry = WeatherData(
            location=row['Location'],
            min_temp=float(row['MinTemp']) if row['MinTemp'] else None,
            max_temp=float(row['MaxTemp']) if row['MaxTemp'] else None,
            rainfall=float(row['Rainfall']) if row['Rainfall'] else None,
            evaporation=float(row['Evaporation']) if row['Evaporation'] else None,
            sunshine=float(row['Sunshine']) if row['Sunshine'] else None,
            wind_gust_dir=row['WindGustDir'] if row['WindGustDir'] else None,
            wind_gust_speed=float(row['WindGustSpeed']) if row['WindGustSpeed'] else None,
            wind_dir_9am=row['WindDir9am'] if row['WindDir9am'] else None,
            wind_dir_3pm=row['WindDir3pm'] if row['WindDir3pm'] else None,
            wind_speed_9am=float(row['WindSpeed9am']) if row['WindSpeed9am'] else None,
            wind_speed_3pm=float(row['WindSpeed3pm']) if row['WindSpeed3pm'] else None,
            humidity_9am=int(row['Humidity9am']) if row['Humidity9am'] else None,
            humidity_3pm=int(row['Humidity3pm']) if row['Humidity3pm'] else None,
            pressure_9am=float(row['Pressure9am']) if row['Pressure9am'] else None,
            pressure_3pm=float(row['Pressure3pm']) if row['Pressure3pm'] else None,
            cloud_9am=int(row['Cloud9am']) if row['Cloud9am'] else None,
            cloud_3pm=int(row['Cloud3pm']) if row['Cloud3pm'] else None,
            temp_9am=float(row['Temp9am']) if row['Temp9am'] else None,
            temp_3pm=float(row['Temp3pm']) if row['Temp3pm'] else None,
            rain_today=row['RainToday'] if row['RainToday'] else None
        )

        # Add the new instance to the session
        db.session.add(weather_entry)

# Commit the session after all entries are added
db.session.commit()
print("Data imported successfully!")
