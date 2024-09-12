import pandas as pd

class DataLoader:
    def __init__(self, file_path: str) -> None:
        """
        Initializes the DataLoader with the path to the CSV file and loads the DataFrame.

        :param file_path: The path to the CSV file to be loaded
        """
        self.file_path = file_path
        #self.df = self.read_csv_pd()
        #print(f"New data has been loaded from {self.file_path} into a DataFrame with shape {self.df.shape}")

    def read_csv_pd(self) -> pd.DataFrame:
        """
        Reads the CSV file and loads it into a pandas DataFrame.

        :return: A pandas DataFrame containing the data from the CSV file
        """
        df = pd.read_csv(self.file_path)
        return df
