import pandas as pd
import logging

class DataLoader:
    def __init__(self, file_path: str, chunk_size=1000) -> None:
        """
        Initializes the DataLoader with the path to the CSV file and loads the DataFrame.

        :param file_path: The path to the CSV file to be loaded
        :param chunk_size: The number of lines to load into each iterator (default = 1000)
        """
        self.logger = logging.getLogger()
        self.logger.debug(f"Initializing DataLoader with file: {file_path}")
        self.file_path = file_path
        self.chunk_size = chunk_size
        self._chunks = []
        self.dataframe = self.chunks_to_dataframe()

    def read_csv_chunks(self):
        """
        Reads in the file and generates an iterator for each chunk.

        :param: self
        """
        self.logger.debug(f"Reading file: {self.file_path}, with chunk size: {self.chunk_size}.")

        try:
            for chunk in pd.read_csv(self.file_path, chunksize=self.chunk_size):
                yield chunk
        except FileNotFoundError as e:
            self.logger.error(f"File not found: {self.file_path}. Error: {str(e)}")
            yield pd.DataFrame()  # Return an empty DataFrame
        except pd.errors.EmptyDataError as e:
            self.logger.error(f"No data to read in the file: {self.file_path}. Error: {str(e)}")
            yield pd.DataFrame()  # Return an empty DataFrame
        except Exception as e:
            self.logger.error(f"An error occurred: {str(e)}")
            yield pd.DataFrame()  # Return an empty DataFrame


    def chunks_to_dataframe(self):
        """
        Takes the generated iterator, appends to a private list then converts the list to a DataFrame that is
        then returned.

        :param: self
        :return: chunky_df
        """
        for chunk in self.read_csv_chunks():
            if not chunk.empty:
                self._chunks.append(chunk)

        # Attempt concatenation of chunks
        if self._chunks:  # Check if there are any chunks to concatenate
            try:
                chunky_df = pd.concat(self._chunks)
            except ValueError as e:
                print(f"ValueError occurred on dataframe creation: {e}")
                self.logger.exception(f"ValueError on chunk to dataframe converter: {e}.")
                return pd.DataFrame()  # Return an empty DataFrame on error
            except TypeError as e:
                print(f"TypeError occurred on dataframe creation: {e}.")
                self.logger.exception(f"TypeError on chunk to dataframe converter: {e}.")
                return pd.DataFrame()  # Return an empty DataFrame on error
        else:
            print("No chunks were loaded. Returning an empty DataFrame.")
            return pd.DataFrame()  # Return an empty DataFrame if no chunks were loaded

        df_no_duplicates = chunky_df.drop_duplicates(subset='row ID', keep='first')
        return df_no_duplicates  # Return the final DataFrame with duplicates removed
