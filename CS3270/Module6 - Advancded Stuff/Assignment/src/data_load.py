from operator import contains
from functools import reduce
import pandas as pd

# Open weather data and save to DataFrame
def read_csv(filepath: str) -> pd.DataFrame:
    """Reads a CSV file and returns a DataFrame.

    Args:
        filepath (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The DataFrame containing the CSV data.
    """
    try:
        # Read the CSV file directly using pandas
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print(f"Error: The file {filepath} was not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file {filepath} is empty.")
    except pd.errors.ParserError:
        print(f"Error: Could not parse the file {filepath}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Use lambda functions to convert temperatures to fahrenheit
def convert_temps(df: pd.DataFrame) -> None:
    """Converts temperature columns in a DataFrame from Celsius to Fahrenheit.
    All this will do it add 4 new columns to the df so we can have the f versions of c.

    Args:
        df (pd.DataFrame): The DataFrame containing weather data.
    """
    try:
        df['MinTemp_F'] = df['MinTemp'].map(lambda x: (x * 9/5) + 32 if pd.notnull(x) else None)
        df['MaxTemp_F'] = df['MaxTemp'].map(lambda x: (x * 9/5) + 32 if pd.notnull(x) else None)
        df['Temp9am_F'] = df['Temp9am'].map(lambda x: (x * 9/5) + 32 if pd.notnull(x) else None)
        df['Temp3pm_F'] = df['Temp3pm'].map(lambda x: (x * 9/5) + 32 if pd.notnull(x) else None)

    # Catch the exceptions
    except KeyError as e:
       print(f"Error: Column {e} not found.")
    except Exception as e:
       print(f"An error occured: {e}")

def filter_by_temperature(df, min_temp=None, max_temp=None):
    """Filters the DataFrame by maximum and/or minimum temperature using map and reduce."""
    conditions = []

    if min_temp is not None:
        conditions.append(df['MaxTemp'] >= min_temp)
    if max_temp is not None:
        conditions.append(df['MaxTemp'] <= max_temp)

    filtered_conditions = list(map(lambda cond: cond if cond is not None else True, conditions))
    combined_condition = reduce(lambda x, y: x & y, filtered_conditions)

    return df[combined_condition]

def group_by_location(df: pd.DataFrame):
    """
    Group weather data by location and calculate mean values for relevant columns.

    Parameters:
    df (DataFrame): The DataFrame containing weather data with a 'Location' column.

    Returns:
    DataFrame: A new DataFrame with mean values for MaxTemp, MinTemp, Rainfall, and Sunshine by Location.
    """
    # Group by 'Location' and calculate mean values
    location_stats = df.groupby('Location').agg({
        'MaxTemp': 'mean',
        'MinTemp': 'mean',
        'Rainfall': 'mean',
        'Sunshine': 'mean'
    }).reset_index()

    return location_stats
