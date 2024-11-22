from app import db

class RequestLog(db.Model):
    """
    Represents a log entry for each request, capturing the query made and
    the timestamp of the request.
    """
    id = db.Column(db.Integer, primary_key=True)
    query = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())


class WeatherData(db.Model):
    """
    Represents weather data records, including various weather attributes such as
    temperature, rainfall, wind, and humidity measurements, categorized by location.
    """
    __tablename__ = 'weather_data'
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(50))
    min_temp = db.Column(db.Float)
    max_temp = db.Column(db.Float)
    rainfall = db.Column(db.Float)
    evaporation = db.Column(db.Float)
    sunshine = db.Column(db.Float)
    wind_gust_dir = db.Column(db.String(10))
    wind_gust_speed = db.Column(db.Float)
    wind_dir_9am = db.Column(db.String(10))
    wind_dir_3pm = db.Column(db.String(10))
    wind_speed_9am = db.Column(db.Float)
    wind_speed_3pm = db.Column(db.Float)
    humidity_9am = db.Column(db.Integer)
    humidity_3pm = db.Column(db.Integer)
    pressure_9am = db.Column(db.Float)
    pressure_3pm = db.Column(db.Float)
    cloud_9am = db.Column(db.Integer)
    cloud_3pm = db.Column(db.Integer)
    temp_9am = db.Column(db.Float)
    temp_3pm = db.Column(db.Float)
    rain_today = db.Column(db.String(3))
