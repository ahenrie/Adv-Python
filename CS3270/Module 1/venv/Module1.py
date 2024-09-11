import pandas as pd
import csv

def load_csv_list(csv_path):
    """
    Load a CSV file into a list of lists.

    Each inner list represents a row in the CSV file.

    :param csv_path: Path to the CSV file.
    :type csv_path: str
    :return: A list of lists where each inner list is a row from the CSV file.
    :rtype: list of list of str
    """
    weather_data_lines = []
    # Open the CSV file for reading
    with open(csv_path, mode="r") as file:
        # Create a CSV reader object
        content = csv.reader(file)
        # Iterate over each row in the CSV file
        for line in content:
            # Append each row (list) to the weather_data_lines list
            weather_data_lines.append(line)
    return weather_data_lines

def load_csv_dataframe(csv_path):
    """
    Load a CSV file into a pandas DataFrame.

    The DataFrame will contain the data from the CSV file,
    with the first row used as the column headers by default.

    :param csv_path: Path to the CSV file.
    :type csv_path: str
    :return: A pandas DataFrame containing the CSV data.
    :rtype: pandas.DataFrame
    """
    # Load the CSV file into a DataFrame
    weather_df = pd.read_csv(csv_path)
    return weather_df

if __name__ == "__main__":
    # Path to the CSV file containing weather data
    csv_path = "../AustraliaWeatherData/Weather Training Data.csv"

    # Load the CSV data into a DataFrame
    df = load_csv_dataframe(csv_path)

    # Load the CSV data into a list of lists
    weather_data = load_csv_list(csv_path)

    # Print DataFrame information (e.g., column names, non-null counts)
    print(df.info())

    # Print the number of rows read into the list
    print(len(weather_data))
