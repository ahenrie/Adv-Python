# Module 4 - Generators/Iterators + Logging Implementation

## Overview

This program processes a CSV file using a generator to yield chunks of data, which are then concatenated into a DataFrame. Users can then view DataFrame information and choose a format and location to save the DataFrame.

## Design Choices

### Generators/Iterators

The `DataLoader` class uses a generator to handle large CSV files efficiently. It reads the CSV file in 1000-line chunks, yielding each chunk (iterator) and concatenating them into a list, which is then converted into a pandas DataFrame. This approach demonstrates an effective use of iterators and iterable concepts, with robust exception handling.

### Exception Handling

Exception handling is implemented in the `DataLoader` class to manage issues during data manipulation. This ensures that data is processed correctly and errors are appropriately logged. The `DataStorage` class also uses exception handling to manage user inputs and file system interactions, addressing potential issues with file paths and permissions.

### Logging

The `logging_config.py` file contains the configuration for logging. All logs are directed to `main_pipeline.log`. The logging setup is designed to allow for easy extension, enabling different modules to log to separate files if needed.

## Usage

1. **Load Data**: Initialize `DataLoader` with the path to a CSV file to load the data.
2. **Process Data**: Pass the loaded DataFrame to `DataProcessor` to compute and display metrics.
3. **Store Data**: Use `DataStorage` to save the processed data in the desired format (CSV, XLSX, JSON).

```python
python3 main.py
```

## Requirements
```bash
pip install openpyxl pandas
```
The correct csv file "AustraliaWeatherData" needs to be in the root of the project directory.

## License
This project is licensed under the [MIT License](LICENSE).
