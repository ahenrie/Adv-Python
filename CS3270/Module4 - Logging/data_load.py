# Generator used here for loading data.
import pandas as pd
import logging

class DataLoader:
    def __init__(self, file_path: str, chunk_size = 1000) -> None:
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
        Reads in the file and generates an iterator for each 1000 lines

        :param: self
        """
        print(f"Reading file: {self.file_path}, with chunk size: {self.chunk_size}.")

        # Iterate over the file in chunks and yield them (generator)
        try:
            for chunk in pd.read_csv(self.file_path, chunksize = self.chunk_size):
                yield chunk
        except FileNotFoundError:
            print("File not found.")
            self.logger.exception("FileNotFoundError occured on chunk generator.")
        except pd.errors.EmptyDataError:
            print("No data to read in the file.")
            self.logger.exception("EmptyDataError occured on chunk generator.")
        except Exception as e:
            print(f"An error occured: {e}.")
            self.logger.exception(f"Error occured on chunk generator: {e}.")

    def chunks_to_dataframe(self):
        """
        Takes the generated iterator appends to a private list then converts the list to a dataframe that is
        then returned.

        :param: self
        :return: chunky_df
        """
        for chunk in self.read_csv_chunks():
            self._chunks.append(chunk)

        # Attempt concatenation of chunks
        try:
            chunky_df = pd.concat(self._chunks)
        # Check columns are lined up correctly between chunks.
        except ValueError as e:
            print(f"ValueError occured on dataframe creation: {e}")
            self.logger.exception(f"ValueError on chunk to dataframe converter: {e}.")
        # Checks the type of chunk being concatenated.
        except TypeError as e:
            print(f"TyperError occured on dataframe creation: {e}.")
            self.logger.exception(f"TypeError on chunk to dataframe converter: {e}.")

        # Return dataframe
        return chunky_df
