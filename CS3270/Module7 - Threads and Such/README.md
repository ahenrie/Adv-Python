# Module 7 - Weather Data Processing Application

## Overview

This application processes weather data from a CSV file, specifically filtering for rows where rain is predicted for tomorrow and calculating average temperatures. The design focuses on efficiency, employing asynchronous data fetching and multiprocessing to handle large datasets effectively.

## Features

- **Asynchronous Data Fetching**: The application reads data from the CSV file in chunks asynchronously, allowing for non-blocking operations. This means that while one chunk is being processed, the application can continue fetching more data, significantly improving overall performance, especially with large files.

- **Multiprocessing for Data Processing**: To further enhance performance, the application utilizes Python's `multiprocessing` module. This allows the program to process multiple chunks of data simultaneously across different CPU cores, maximizing CPU utilization. By filtering the data and calculating averages concurrently, the application speeds up compute-intensive tasks, resulting in faster execution times.

## How It Works

1. **Data Fetching**: The `DataFetcher` class reads the weather data from a CSV file in defined chunk sizes. This prevents loading the entire dataset into memory at once, making the application scalable and efficient for large datasets.

2. **Data Processing**: After fetching, the application processes the data using the `DataProcessor` class. This class contains methods to filter out rows based on specific criteria (like rain predictions) and calculate average temperatures (which I hope to get working in a later release). The use of multiprocessing allows these tasks to be distributed across available CPU cores, reducing the time required for data processing.

3. **Output**: The processed data is aggregated into a final DataFrame, which can then be analyzed or exported as needed.

## Getting Started

To run the application, ensure you have the necessary dependencies installed. You can do this by running:

```bash
pip install pandas aiofiles
```

Then, execute the application:

```bash
python main.py
```

Make sure to have the `Weather Training Data.csv` file in the same directory as the application for it to function correctly.

### What Should I See?
Depdening on the size of chunks used, more chunks are needed to store the data to be processed on. For example with a chunk size of 100 we see:
```bash
Processing chunk 0
Processing chunk 1
Processing chunk 2
Processing chunk 3
Processing chunk 4
Processing chunk 5
Processing chunk 6
Processing chunk 7
Processing chunk 8
Processing chunk 9
Processing chunk 10
Processing chunk 11
Processing chunk 12
Processing chunk 13
Processing chunk 14
Processing chunk 15
Processing chunk 16
Processing chunk 17
Processing chunk 18
Processing chunk 19
Processing chunk 20
Processing chunk 21
Processing chunk 22
Processing chunk 23
Processing chunk 0
Processing chunk 24
Processing chunk 25
```

But with a larger chunk size of 1000 we do not need as many chunks so we get:

```bash
Processing chunk 0
Processing chunk 1
Processing chunk 2
Processing chunk 0
Processing chunk 1
Processing chunk 2
Processing chunk 0
Processing chunk 1
Processing chunk 2
Processing chunk 0
Processing chunk 1
Processing chunk 2
Processing chunk 0
Processing chunk 1
Processing chunk 2
Processing chunk 0
Processing chunk 1
```

The last output should be a comparison of pulling the entire CSV into memory, applying the same filter we do during processing, and then printing the lengths:

```bash
Length of filtered chuncks:  22359
Length of full data dataframe:  99516
Length of filtered pandas fetched dataframe:  22359
```
The first length is the data that is fetched and processed asynchronsouly and with the help of multithreading. The second is the CSV into a dataframe and the last is the filtered CSV dataframe.

## Conclusion

By combining asynchronous data fetching and multiprocessing, this application achieves significant performance improvements in processing weather data. This approach allows for efficient handling of large datasets while fully utilizing modern multi-core processors, making it suitable for various data analysis tasks.

## License
This project is licensed under the [MIT License](LICENSE).
