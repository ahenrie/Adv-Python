from data_load import DataLoader
from data_processing import DataProcessor
from data_storage import DataStorage

class DataPipeLine:
    def __init__(self, data_loader: DataLoader, data_processor: DataProcessor, data_storage: DataStorage) -> None:
        """
        Initializes the DataPipeLine with instances of DataLoader, DataProcessor, and DataStorage.

        :param data_loader: An instance of DataLoader for loading data
        :param data_processor: An instance of DataProcessor for processing data
        :param data_storage: An instance of DataStorage for storing data
        """
        self.data_loader = data_loader
        self.data_processor = data_processor
        self.data_storage = data_storage

    def run_pipeline(self) -> None:
        """
        Executes the data pipeline by performing the following steps:
        1. Load data using the DataLoader instance.
        2. Process the data using the DataProcessor instance.
        3. Store the processed data using the DataStorage instance.
        """
        try:
            df = self.data_loader.read_csv_chunks()
            print("Data loaded successfully.")
        except Exception as e:
            print(f"An unexpected error occured when loading data: {e}.")

        try:
            self.data_processor.process_data_frame()
            print("Data processed successfully.")
        except Exception as e:
            print(f"An unexpected error occured when processing the data: {e}.")

        try:
            self.data_storage.get_file_type()
        except Exception as e:
            print(f"An unexpected error occured on storage: {e}.")
