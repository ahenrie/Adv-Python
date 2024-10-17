import pandas as pd
import multiprocessing

class DataProcessor:
    """A class for processing weather data with methods to filter and compute averages,
    using multiprocessing to handle large datasets efficiently."""

    def __init__(self):
        """
        Initializes the DataProcessor with a chunk counter.

        Args:
            None

        Returns:
            None
        """
        self.chunk_number = 0

    def filter_rain_data(self, chunk):
        """
        Filters data to include only rows where rain is predicted for tomorrow.

        Args:
            chunk (list or DataFrame-like): A chunk of data to process, typically a subset
            of the full dataset.

        Returns:
            pandas.DataFrame: A DataFrame containing only the rows where 'RainTomorrow'
            equals '1'.

        Side Effects:
            Prints the chunk number being processed to the console.
        """
        print(f"Processing chunk {self.chunk_number}")
        self.chunk_number += 1
        df = pd.DataFrame(chunk)

        # Clean up the column names by removing extra quotes and spaces
        df.columns = df.columns.str.replace('"', '').str.strip()

        # Filter rows where 'RainTomorrow' equals '1'
        filtered_data = df[df['RainTomorrow'] == '1']

        return filtered_data

    """ Sample of what I would like to create with some sort of aggregate.
    def avg_temp_data(self, chunk):

        Calculates the average of the minimum and maximum temperatures in a data chunk.

        Args:
            chunk (list or DataFrame-like): A chunk of data containing temperature columns.

        Returns:
            pandas.Series: A Series containing the average of 'MinTemp' and 'MaxTemp'
            for the chunk.

        df = pd.DataFrame(chunk)

        # Calculate the mean of 'MinTemp' and 'MaxTemp' columns
        avg_temp = df[['MinTemp', 'MaxTemp']].mean()

        return avg_temp
    """

    def process_in_parallel(self, chunks, func):
        """
        Processes data chunks in parallel using the provided function.

        Args:
            chunks (list): A list of data chunks to be processed.
            func (callable): A function that processes a single chunk
            (e.g., filter_rain_data or avg_temp_data).

        Returns:
            list: A list of results obtained by applying the provided function to each chunk.
        """
        with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
            results = pool.map(func, chunks)

        return results
