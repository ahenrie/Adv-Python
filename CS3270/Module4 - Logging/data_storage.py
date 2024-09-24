import pandas as pd
import logging

class DataStorage:
    def __init__(self, df) -> None:
        """
        Initializes the DataStorage with a DataFrame and prompts for file storage options.

        :param df: DataFrame containing the data to be stored
        """
        self.logger = logging.getLogger()
        self.df = df
        self.out_file_path = None
        logging.info("DataStorage initialized with DataFrame.")

    def get_file_type(self):
        """
        Prompts the user to choose a file type and saves the DataFrame to the chosen format.
        The method will repeatedly prompt until a valid file type is selected.
        """
        self.out_file_path = input("Enter the file path (without extension): ")
        logging.info(f"User provided file path: {self.out_file_path}")

        while True:
            decision = input("What file type would you like to save your DataFrame to (CSV, XLSX, JSON): ").upper()
            logging.info(f"User selected file type: {decision}")

            try:
                match decision:
                    case "CSV":
                        self.out_file_path += ".csv"
                        self.df.to_csv(self.out_file_path, index=False)
                        logging.info(f"Data saved as CSV to {self.out_file_path}")
                        print(f"Data has been saved as a CSV to {self.out_file_path}")
                        break
                    case "XLSX":
                        self.out_file_path += ".xlsx"
                        self.df.to_excel(self.out_file_path, index=False)
                        logging.info(f"Data saved as Excel file to {self.out_file_path}")
                        print(f"Data has been saved as an Excel file to {self.out_file_path}")
                        break
                    case "JSON":
                        self.out_file_path += ".json"
                        self.df.to_json(self.out_file_path, orient='records')
                        logging.info(f"Data saved as JSON to {self.out_file_path}")
                        print(f"Data has been saved as a JSON to {self.out_file_path}")
                        break
                    case _:
                        logging.warning(f"Unsupported file type '{decision}' chosen by user.")
                        print(f"File type '{decision}' is not supported. Please choose CSV, XLSX, or JSON.")
            except FileNotFoundError:
                logging.error(f"FileNotFoundError: The specified file path '{self.out_file_path}' could not be found.")
                print("Error: The specified file path could not be found.")
                self.out_file_path = input("Please enter a valid file path (without extension): ")
            except PermissionError:
                logging.error(f"PermissionError: You do not have permission to save to '{self.out_file_path}'.")
                print("PermissionError: You do not have permission to save to this path.")
                self.out_file_path = input("Please enter a different file path (without extension): ")
            except OSError as e:
                logging.error(f"OSError: {e}")
                print(f"OSError: {e}. Please enter a different path that allows writing.")
                self.out_file_path = input("Please enter a different file path (without extension): ")
            except pd.errors.EmptyDataError:
                logging.error("EmptyDataError: No data to write from the DataFrame.")
                print("No data to write from the DataFrame.")
                break
            except Exception as e:
                logging.exception("An unexpected error occurred during file saving.")
                print(f"An unexpected error occurred: {e}")
                break
