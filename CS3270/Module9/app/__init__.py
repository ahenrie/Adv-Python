from flask import Flask
from app.extensions import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Import and register routes
    from app.routes import index, weather_data, predict
    app.add_url_rule('/', view_func=index, methods=['GET', 'POST'])
    app.add_url_rule('/weather_data', view_func=weather_data)
    app.add_url_rule('/predict', view_func=predict, methods=['GET', 'POST'])

    return app
