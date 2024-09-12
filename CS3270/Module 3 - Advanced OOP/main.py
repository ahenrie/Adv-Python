from data_load import DataLoader
from data_processing import DataProcessor
from data_storage import DataStorage

def main():
    load_data = DataLoader("../AustraliaWeatherData/Weather Test Data.csv")
    process_data = DataProcessor(DataLoader.read_csv_pd(load_data))
    store_data =DataStorage(DataLoader.read_csv_pd(load_data))


if __name__ == "__main__":
    main()
