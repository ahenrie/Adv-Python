import pandas as pd

class DataStorage:
    def __init__(self, df) -> None:
        """
        Initializes the DataStorage with a DataFrame and prompts for file storage options.

        :param df: DataFrame containing the data to be stored
        """
        self.df = df
        self.out_file_path = None

    def get_file_type(self):
        """
        Prompts the user to choose a file type and saves the DataFrame to the chosen format.
        The method will repeatedly prompt until a valid file type is selected.
        """
        self.out_file_path = input("Enter the file path (without extension): ")

        while True:
            decision = input("What file type would you like to save your DataFrame to (CSV, XLSX, JSON): ").upper()

            # Attempt to save the file based on user's input
            try:
                match decision:
                    case "CSV":
                        self.out_file_path += ".csv"
                        self.df.to_csv(self.out_file_path, index=False)
                        print(f"Data has been saved as a CSV to {self.out_file_path}")
                        break
                    case "XLSX":
                        self.out_file_path += ".xlsx"
                        self.df.to_excel(self.out_file_path, index=False)
                        print(f"Data has been saved as an Excel file to {self.out_file_path}")
                        break
                    case "JSON":
                        self.out_file_path += ".json"
                        self.df.to_json(self.out_file_path, orient='records')
                        print(f"Data has been saved as a JSON to {self.out_file_path}")
                        break
                    case _:
                        print(f"File type '{decision}' is not supported. Please choose CSV, XLSX, or JSON.")
            except FileNotFoundError:
                print(f"Error: The specified file path '{self.out_file_path}' could not be found.")
                # Reset out_file_path and allow the user to re-enter a valid path
                self.out_file_path = input("Please enter a valid file path (without extension): ")
            except PermissionError:
                print(f"PermissionError: You do not have permission to save to '{self.out_file_path}'.")
                # Allow the user to re-enter a valid file path
                self.out_file_path = input("Please enter a different file path (without extension): ")
            except pd.errors.EmptyDataError:
                print(f"EmptyDataError: No data to write from the DataFrame.")
                break
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                break
