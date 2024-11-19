from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    """
    Create and configure the Flask application.

    Configures the database connection and initializes the SQLAlchemy
    extension. Registers the index and weather_data routes with the app.

    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../data/weather.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from app.routes import index, weather_data

    app.add_url_rule("/", view_func=index, methods=["GET", "POST"])
    app.add_url_rule("/weather", view_func=weather_data)

    return app
