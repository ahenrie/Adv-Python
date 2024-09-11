import pandas as pd

def read_csv_pd(file_path):
  """
  This function reads a CSV file into a pandas DataFrame.

  Args:
      file_path (str): The path to the CSV file.

  Returns:
      pandas.DataFrame: The DataFrame containing the data from the CSV file.
  """
  df = pd.read_csv(file_path)
  return df

def get_df_info(df):
  """
  This function gets general information about a pandas DataFrame.

  Args:
      df (pandas.DataFrame): The DataFrame to get information about.

  Returns:
      str: A string containing information about the DataFrame,
          including data types and non-null values.
  """
  info = df.info()
  return info

def average_min_temp(df, column_name):
  """
  This function calculates the average of a specific column in a DataFrame,
  rounding the result to two decimal places.

  Args:
      df (pandas.DataFrame): The DataFrame containing the temperature data.
      column_name (str): The name of the column containing the minimum temperatures.

  Returns:
      float: The average minimum temperature, rounded to two decimal places.
  """
  average_temp = df[column_name].mean().round(2)
  return average_temp

def median_max_temp(df, column_name):
  """
  This function calculates the median of a specific column in a DataFrame,
  rounding the result to two decimal places.

  Args:
      df (pandas.DataFrame): The DataFrame containing the temperature data.
      column_name (str): The name of the column containing the maximum temperatures.

  Returns:
      float: The median maximum temperature, rounded to two decimal places.
  """
  median_temp = df[column_name].median().round(2)
  return median_temp

def mode_max_temp(df, column_name):
  """
  This function finds the mode (most frequent value) of a specific column in a DataFrame.

  Args:
      df (pandas.DataFrame): The DataFrame containing the temperature data.
      column_name (str): The name of the column containing the maximum temperatures.

  Returns:
      pandas.Series: The mode(s) of the maximum temperatures.
  """
  mode_max = df[column_name].mode()
  return mode_max

def pretty_print(df):
  """
  This function prints formatted information about a weather DataFrame,
  including data info and temperature metrics.

  Args:
      df (pandas.DataFrame): The DataFrame containing the weather data.
  """
  print("Info regarding your weather CSV:")
  print(get_df_info(df))
  print("\n********************* Temperature Metrics *********************")
  print(f"Average minimum temperature: {average_min_temp(df, 'MinTemp')} °C")
  print(f"Average maximum temperature: {median_max_temp(df, 'MaxTemp')} °C")
  print(f"Mode maximum temperature: {mode_max_temp(df, 'MaxTemp')} Celsius")
