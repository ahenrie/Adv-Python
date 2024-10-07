# Project 6

## Overview

Since this project was less about object orientation programming, I focused more on using lambda functions, filtering, maps, and reduce with the large AustraliaWeatherData. I did include some testing that I will go over later.
It was strange not putting everything in classes at first. Functional programming is something I would like to explore some more.

## Modules

### data_load

This module contains the loading of the CSV into a DataFrame and some cool functions!

 - `read_csv(filepath: str)`: Reads the CSV file and returns a pandas DataFrame.
 - `convert_temps(df: pd.DataFrame)`: Converts the temperatures in Celsius to Fahrenheit using lambda functions.
 - `filter_by_temperature(df, min_temp=None, max_temp=None)`: Filters the DataFrame by maximum and/or minimum temperature.
 - `group_by_location(df: pd.DataFrame)`:Groups weather data by location and calculate mean values for relevant columns.

### data_vis

This module is used for displaying and creating the visualizations.

 - `visualize_temperature_trends(df)`: Plots the temperature trends using a line plot.
 - `visualize_location_stats(location_stats_df)`: Visualizes average temperatures and rainfall by location.
 - `create_special_chart(df, min_temp=None, max_temp=None)`: Creates a bar chart showing average weather metrics by location after filtering.

### data_load_tests

The data_load_tests.py module contains unit tests designed to verify the functionality of the data_load.py module. The tests ensure that the data loading, temperature conversion, and filtering functions work correctly.

 - `setUp(self) -> None`: Creates two DataFrames, one from the actual data, and one with some tests data.
 - `test_new_columns(self)`: Is very simple and tests that new columns have been created for the new temperatures.
 - `test_convert_temps_complete(self)`: Tests the conversions with the small testing DataFrame that is setup earlier.
 - `test_temp_conversions(self)`: Iterates through each conversion and ensures that the conversion from Celsius is completed and accurate.

## Requirements

- Pandas 3.x
- Seaborn
- Matplotlib
- Unittest

## Usage
**Please have the correct CSV at the root of the project an a correct folder name that matches the filepath in the main().**

To execute the main function:

```bash
python3 main.py
```

## License
This project is licensed under the [MIT License](LICENSE).
