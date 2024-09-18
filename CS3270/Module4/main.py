from data_load import DataLoader
from data_processing import DataProcessor
from data_storage import DataStorage
from data_pipeline import DataPipeLine

import pandas as pd

def main():
    load_data = DataLoader("../AustraliaWeatherData/Weather Test Data.csv")
    process_data = DataProcessor(load_data.dataframe)
    store_data = DataStorage(load_data.dataframe)

    pipline = DataPipeLine(load_data, process_data, store_data)
    pipline.run_pipeline()

if __name__ == "__main__":
    main()
