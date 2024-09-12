# Data Pipeline Project with OOP - Module 3

## Overview

This project implements a data pipeline for loading, processing, and storing weather data using Object-Oriented Programming (OOP) principles in Python. The pipeline is designed to be modular and extensible, allowing for easy maintenance and future enhancements.
I originally wrote this program to chain constructors but it made the DataPipeline class difficult to implement.

## Design Choices

### OOP Principles Applied

1. **Encapsulation**: Each class encapsulates a specific responsibility:
   - `DataLoader` handles loading data from a CSV file.
   - `DataProcessor` processes the DataFrame to compute metrics.
   - `DataStorage` manages saving the DataFrame in various formats.

   By encapsulating these responsibilities, each class maintains its own state and behavior, providing a clear interface for interacting with different parts of the data pipeline.


3. **Polymorphism**: Achieved through the `DataStorage` class’s `get_file_type` method, which handles multiple file formats (CSV, XLSX, JSON) based on user input. This demonstrates polymorphism by executing different code paths depending on the file format chosen.

4. **Abstraction**: Each class abstracts away the details of its operations:
   - `DataLoader` abstracts the details of reading a CSV file.
   - `DataProcessor` abstracts the details of computing statistics.
   - `DataStorage` abstracts the details of saving data in different formats.

   Users interact with high-level methods without needing to understand the underlying implementation.

### Python Syntax and Behaviors

- **Class Definitions**: Classes such as `DataLoader`, `DataProcessor`, and `DataStorage` are defined to encapsulate functionality related to their specific tasks. This modular approach allows for clear separation of concerns.

- **Constructor Method (`__init__`)**: Each class uses the constructor to initialize its state. For example, `DataLoader` initializes the file path and loads the data, while `DataProcessor` initializes with a DataFrame and processes it.

- **Instance Methods**: Methods like `read_csv_pd`, `process_data_frame`, and `get_file_type` are defined to operate on the instance’s state. These methods implement the core functionality and interact with the instance attributes.

- **Input Handling and User Interaction**: The `DataStorage` class uses the `input` function to interact with the user, asking for file format preferences and validating the input.

- **Polymorphic Behavior**: In `DataStorage`, the `get_file_type` method demonstrates polymorphism by handling different file formats. The method uses a `match` statement to choose the appropriate file-saving method based on user input.

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
