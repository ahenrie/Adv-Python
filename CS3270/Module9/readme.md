
# Weather Data Application

This is a Flask-based application designed to handle weather data, including importing weather data from CSV files, storing it in an SQLite database, and allowing users to view and search weather data by location. The application also includes functionality to query and manage the data, as well as a dark theme UI for user interaction.

## Features

- **Location Search**: Users can select a location from a dropdown to view specific weather data.
- **View All Data**: A page to view all weather data in the database.
- **Data Import**: Ability to import weather data from CSV weather files into the database.
- **Dark Theme UI**: The application has a modern dark theme UI for enhanced user experience.
- **Unit Testing**: Tests to ensure the correct functionality of various features.

## Routes

### `/` (Root Route)
- **Method**: GET, POST
- **Description**: The root route displays a form that allows users to select a location from a dropdown list. The dropdown contains unique locations fetched from the weather data database.
  - **GET request**: Renders the `index.html` template with a list of locations available for selection.
  - **POST request**: If a user selects a location and submits the form, the route redirects to `/weather`, passing the selected location as a query parameter.

- **Functionality**:
  - Displays a form to select a location.
  - On form submission (POST), redirects to the `weather_data` route with the selected location.

---

### `/weather` (Weather Data Route)
- **Method**: GET
- **Description**: This route displays the weather data for the selected location or all weather data if no location is provided in the query parameter.
  - If a location is specified via a query parameter (`location`), the route filters the weather data for that location.
  - If no location is specified, the route returns all weather data available in the database.

- **Functionality**:
  - Displays the weather data either for a specific location or for all locations.
  - Filters the weather records based on the `location` query parameter if provided.

---

## Requirements

- Flask==3.0.3
- Flask-SQLAlchemy==3.1.1
- pytest==8.3.3
- python-dateutil==2.9.0.post0
- SQLAlchemy==2.0.36


## Installation

1. Install Depdencies

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. To start the Flask application:

   ```bash
   flask run
   ```

   This will start the application on `http://127.0.0.1:5000`.

2. Navigate to the application in your browser.

3. To import weather data from a CSV file, use the import script provided in the project. (This may need to be done first if the weather.db is not in the data directory.)

   Example command:
   ```bash
   python import_csv.py
   ```
**NOTE**: This script to import the csv file is meant for specific csv file in the data directory!


4. Use the search feature to view data for specific locations or view all weather data.
  The view all weather data option will take a little while to load as it is loading every location.

## Tests

The application includes several unit tests, including:

- **Test the POST request for each location in the index route.**
- **Test that each location has data in the database after import.**

To run the tests, use the following command:

```bash
pytest -v
```

## License

This project is licensed under the MIT License
