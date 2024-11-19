import pytest
from app import create_app, db
from app.models import WeatherData
from sqlalchemy import text

@pytest.fixture
def app():
    """Set up the Flask app for testing."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for tests

    with app.app_context():
        db.create_all()
        # Add sample data to test locations
        sample_data = [
            {"location": "Location1", "min_temp": 15.0, "max_temp": 25.0},
            {"location": "Location2", "min_temp": 17.0, "max_temp": 27.0},
            {"location": "Location3", "min_temp": 10.0, "max_temp": 20.0}
        ]
        for entry in sample_data:
            db.session.add(WeatherData(**entry))
        db.session.commit()
    yield app

    # Clean up after tests
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    """Set up a test client for making requests."""
    return app.test_client()

def test_each_location_has_data(app):
    """Run SQL statements to verify that each location has data."""
    with app.app_context():
        # Fetch distinct locations from the database and run SQL checks
        locations = db.session.query(WeatherData.location).distinct().all()

        for loc in locations:
            loc_name = loc[0]
            sql_query = text("SELECT COUNT(*) FROM weather_data WHERE location = :loc")
            result = db.session.execute(sql_query, {"loc": loc_name}).scalar()

            # Assert that there is at least one record for each location
            assert result > 0, f"No data found for location {loc_name}"
