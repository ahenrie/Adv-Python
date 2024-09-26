# Module 5 Unit Testing

## Overview of Testing Framework

The project uses the `unittest` framework, a built-in Python module that allows for the creation and running of tests. This framework provides a robust structure for organizing tests and a variety of assertions to verify expected outcomes.
I have always used PyTest so I wanted to try something different.

## Test Files

The unit tests are organized into separate files corresponding to each module:

- **`data_load_tests.py`**: tests the `DataLoader` class, ensuring it can read and process CSV data correctly.
- **`data_storage_tests.py`**: tests for the `DataStorage` class, validating its functionality in saving data in different formats (CSV, Excel, JSON).
- **`data_processor_tests.py`**: tests the `DataProcessor` class, verifying its ability to calculate statistical measures from the DataFrame.
- **`data_pipeline_tests.py`**: tests the `DataPipeLine` class, ensuring the entire pipeline functions as expected.

## Key Testing Features

### DataLoader Tests

In this testsuite, I wanted to focus on testing the correct reading of data so I used the large data set in this testing module. You can see where I used smaller simpler dataframes in the other test modules to make the testing faster and straightforward.

- **Initialization**: Validates that an instance of `DataLoader` is created successfully, and checks that essential attributes (like chunks and file path) are correctly initialized.
- **Chunk Reader**: Tests the `read_csv_chunks` method to ensure it returns a generator and that the size of the returned chunks is as expected.
- **DataFrame Conversion**: Verifies that the chunks read from the CSV are correctly converted into a Pandas DataFrame.
- **Error Handling**: Includes tests for edge cases, such as handling an empty CSV file and a non-existent file.(I could make more tests as I get logs from users.)

### DataStorage Tests

This testsuite is very straight forward. The while loop makes it impossible to select anything other than the csv, excel, and json file types so I focused on testing those. I tried my best with MagicMock. I want to explore using that library some more.

- **File Format Saving**: Uses mocking to simulate user input and verify that the correct saving methods (`to_csv`, `to_excel`, `to_json`) are called with the appropriate parameters based on the chosen file type.

### DataProcessor Tests

Since the `DataProcessor` prints some info about the dataframe, it was simple to tests.

- **Statistical Calculations**: Tests methods that calculate the average, median, and mode of temperature data, ensuring they return the correct values.
- **DataFrame Information Retrieval**: Confirms that the `get_df_info` method calls the DataFrame's `info()` method, ensuring accurate data retrieval.

### DataPipeLine Tests

The `DataPipeLine` class is really a main program that I call in main to keep main clean. It does not need as much testing since it is built on already tested classes, but I made a testsuite for the class anyways.

- **Pipeline Execution**: Tests the `run_pipeline` method to verify that it successfully orchestrates the loading, processing, and storing of data, while handling exceptions appropriately at each step.

## Test Usage

To execute the unit tests, run the following command in your terminal:

```bash
python -m unittest discover -s tests -p "*.py"
```

## License
This project is licensed under the [MIT License](LICENSE).
