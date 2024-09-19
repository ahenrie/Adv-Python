import logging

class DataProcessor:
    def __init__(self, df) -> None:
        """
        Initializes the DataProcessor with a DataFrame and processes the data.

        :param df: DataFrame containing the weather data to be processed
        """
        self.logger = logging.getLogger()
        self.df = df  # Store the DataFrame as an instance attribute

    def get_df_info(self):
        """
        Retrieves and returns the summary information of the DataFrame.

        :return: Summary information about the DataFrame
        """
        info = self.df.info()
        return info

    def average_min_temp(self):
        """
        Calculates and returns the average minimum temperature from the DataFrame.

        :return: Average minimum temperature rounded to two decimal places
        """
        average_mt = self.df['MinTemp'].mean().round(2)
        return average_mt

    def median_max_temp(self):
        """
        Calculates and returns the median maximum temperature from the DataFrame.

        :return: Median maximum temperature rounded to two decimal places
        """
        median_temp = self.df['MaxTemp'].mean().round(2)
        return median_temp

    def mode_max_temp(self):
        """
        Calculates and returns the mode (most frequent value) of maximum temperature from the DataFrame.

        :return: Mode of maximum temperature rounded to two decimal places
        """
        mode_max = self.df['MaxTemp'].mode().round(2)
        return mode_max

    def process_data_frame(self):
        """
        Processes the DataFrame to print out temperature metrics and DataFrame information.
        """
        self.logger.debug(f"All DataProcessor methods completed successfully.")
        print("Info regarding your weather CSV:")
        print("\n********************* Temperature Metrics *********************")
        print(f"Average minimum temperature: {self.average_min_temp()} °C")
        print(f"Average maximum temperature: {self.median_max_temp()} °C")
        print(f"Mode maximum temperature: {self.mode_max_temp()}")
        print("\n********************* Column Information **********************")
        print(self.get_df_info())
