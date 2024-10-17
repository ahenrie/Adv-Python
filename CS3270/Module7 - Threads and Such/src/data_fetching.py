import asyncio
import aiofiles
import csv
import pandas as pd
from multiprocessing import Pool, cpu_count
from .data_processing import DataProcessor

class DataFetcher:
    """
    A class responsible for fetching and processing CSV data in chunks,
    utilizing asynchronous I/O and multiprocessing for efficiency.
    """

    def __init__(self, file_path: str, chunk_size: int = 1000) -> None:
        """
        Initializes the DataFetcher with the file path and chunk size.

        Args:
            file_path (str): The path to the CSV file.
            chunk_size (int): The number of rows per chunk (default is 1000).

        Returns:
            None
        """
        self.file_path = file_path
        self.chunk_size = chunk_size
        self.processor = DataProcessor()

    async def read_csv_in_chunks(self):
        """
        Asynchronously reads a CSV file in chunks, yielding each chunk.

        This method reads the CSV file line by line, accumulating rows into
        chunks based on the specified chunk size. Once a chunk is complete,
        it yields the chunk.

        Args:
            None

        Yields:
            list[dict]: A list of dictionaries, where each dictionary represents
            a row from the CSV file with column names as keys.

        Side Effects:
            Opens the CSV file asynchronously for reading.
        """
        async with aiofiles.open(self.file_path, mode='r') as f:
            # Read the header asynchronously to get column names
            header = await f.readline()
            fieldnames = header.strip().split(',')
            chunk = []

            async for line in f:
                # Create a dictionary for each row using the header as keys
                row = dict(zip(fieldnames, line.strip().split(',')))
                chunk.append(row)

                # Yield the chunk when it reaches the specified size
                if len(chunk) >= self.chunk_size:
                    yield chunk
                    chunk = []

            # Yield any remaining rows that didn’t complete a full chunk
            if chunk:
                yield chunk

    async def process_chunks(self):
        """
        Asynchronously processes all data chunks in parallel.

        This method fetches chunks using `read_csv_in_chunks` and processes
        them in parallel using the `filter_rain_data` method from DataProcessor.

        Args:
            None

        Returns:
            list[pandas.DataFrame]: A list of DataFrames, each containing
            filtered data from one chunk.

        Side Effects:
            Utilizes multiprocessing to process chunks in parallel.
        """
        chunks = []

        # Collect all chunks asynchronously
        async for chunk in self.read_csv_in_chunks():
            chunks.append(chunk)

        # Process the chunks in parallel using DataProcessor's method
        processed_chunks = self.processor.process_in_parallel(
            chunks, self.processor.filter_rain_data
        )

        return processed_chunks
