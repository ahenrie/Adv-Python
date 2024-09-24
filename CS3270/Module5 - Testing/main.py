from data_load import DataLoader
from data_processing import DataProcessor
from data_storage import DataStorage
from data_pipeline import DataPipeLine
import pandas as pd
import logging
from logging_config import setup_logging  # Import the logging setup function

def main():
    setup_logging()

    logging.info("Starting main pipeline")

    # Debugging and error handling for loading data
    try:
        logging.debug("Attempting to load data from file")
        load_data = DataLoader("../AustraliaWeatherData/Weather Test Data.csv")
        logging.info(f"Data successfully loaded with shape {load_data.dataframe.shape}")
    except FileNotFoundError:
        logging.error("The file was not found at the specified path.")
        return
    except pd.errors.EmptyDataError:
        logging.error("The file is empty.")
        return
    except Exception as e:
        logging.exception(f"Unexpected error occurred while loading data: {e}")
        return

    # Debugging and error handling for processing data
    try:
        logging.debug("Attempting to process data")
        process_data = DataProcessor(load_data.dataframe)
        logging.info("Data successfully processed")
    except Exception as e:
        logging.exception(f"Unexpected error occurred while processing data: {e}")
        return

    # Debugging and error handling for storing data
    try:
        logging.debug("Attempting to store data")
        store_data = DataStorage(load_data.dataframe)
        logging.info("Data storage initialized successfully")
    except Exception as e:
        logging.exception(f"Unexpected error occurred while initializing data storage: {e}")
        return

    # Debugging for running the pipeline
    try:
        logging.debug("Running the data pipeline")
        pipline = DataPipeLine(load_data, process_data, store_data)
        pipline.run_pipeline()
        logging.info("Pipeline completed successfully")
    except Exception as e:
        logging.exception(f"Unexpected error occurred while running the pipeline: {e}")
        return

if __name__ == "__main__":
    main()
