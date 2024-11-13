import csv
from app import db, create_app
from app.models import WeatherData

def import_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            weather_data = WeatherData(
                location=row['Location'],
                min_temp=row['MinTemp'],
                max_temp=row['MaxTemp'],
                rainfall=row['Rainfall'] if row['Rainfall'] else None,  # Handle missing values
                evaporation=row['Evaporation'] if row['Evaporation'] else None,
                sunshine=row['Sunshine'] if row['Sunshine'] else None,
                wind_gust_dir=row['WindGustDir'],
                wind_gust_speed=row['WindGustSpeed'] if row['WindGustSpeed'] else None,
                wind_dir_9am=row['WindDir9am'],
                wind_dir_3pm=row['WindDir3pm'],
                wind_speed_9am=row['WindSpeed9am'] if row['WindSpeed9am'] else None,
                wind_speed_3pm=row['WindSpeed3pm'] if row['WindSpeed3pm'] else None,
                humidity_9am=row['Humidity9am'] if row['Humidity9am'] else None,
                humidity_3pm=row['Humidity3pm'] if row['Humidity3pm'] else None,
                pressure_9am=row['Pressure9am'] if row['Pressure9am'] else None,
                pressure_3pm=row['Pressure3pm'] if row['Pressure3pm'] else None,
                cloud_9am=row['Cloud9am'] if row['Cloud9am'] else None,
                cloud_3pm=row['Cloud3pm'] if row['Cloud3pm'] else None,
                temp_9am=row['Temp9am'],
                temp_3pm=row['Temp3pm'],
                rain_today=row['RainToday']
            )
            db.session.add(weather_data)
        db.session.commit()

# Create the app and push an application context
app = create_app()
with app.app_context():
    import_csv('data/Weather Test Data.csv')  # Update the path if necessary
