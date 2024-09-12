import pandas as pd

class DataLoader:

    def __init__(self, file_path):
        self.file_path = file_path  # Initialize file_path
        self.df = self.read_csv_pd()  # Load the DataFrame
        print(f"New data has been loaded from {self.file_path} into a DataFrame with shape {self.df.shape}")  # Access after initialization

    def read_csv_pd(self):
        df = pd.read_csv(self.file_path)  # Load the CSV file into a DataFrame
        return df
