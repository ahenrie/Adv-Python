class DataStorage:
    def __init__(self, df) -> None:
        self.df = df
        self.out_file_path = None
        self.get_file_type()

    def get_file_type(self):
        # Ask the user for the file path (without extension)
        self.out_file_path = input("Enter the file path (without extension): ")

        # Loop until a valid file type is provided
        while True:
            decision = input("What file type would you like to save your data frame to (CSV, XLSX, JSON): ").upper()

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
