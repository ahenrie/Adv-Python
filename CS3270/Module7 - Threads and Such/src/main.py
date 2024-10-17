import asyncio
from src.data_fetching import DataFetcher
import pandas as pd
from multiprocessing import cpu_count

async def main():
    """
    Main function to fetch and process weather data asynchronously.

    It fetches the data in chunks, filters for rain data, and calculates
    the average temperature for each chunk using multiprocessing.
    """
    # Create an instance of DataFetcher for the CSV file
    data_fetcher = DataFetcher("Weather Training Data.csv", 1000)

    # Process the chunks of data asynchronously
    processed_chunks = await data_fetcher.process_chunks()

    # Combine the filtered chunks into a single DataFrame
    filtered_df = pd.concat(processed_chunks)

    # Show the difference between a df with all of the data
    all_df = pd.read_csv("Weather Training Data.csv")
    pandas_filtered_df = all_df[all_df['RainTomorrow'] == 1]

    print(f"Length of filtered chuncks: ", len(filtered_df))
    print(f"Length of full data dataframe: ", len(all_df))
    print(f"Length of filtered pandas fetched dataframe: ", len(pandas_filtered_df))


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"An error occurred: {e}")
