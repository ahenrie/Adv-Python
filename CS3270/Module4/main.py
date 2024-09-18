from data_load import DataLoader
from data_processing import DataProcessor
from data_storage import DataStorage
from data_pipeline import DataPipeLine

def main():
    load_data = DataLoader("../AustraliaWeatherData/Weather Test Data.csv")
    process_data = DataProcessor(DataLoader.read_csv_pd(load_data))
    store_data =DataStorage(DataLoader.read_csv_pd(load_data))

    pipline = DataPipeLine(load_data, process_data, store_data)
    pipline.run_pipeline()

if __name__ == "__main__":
    main()
