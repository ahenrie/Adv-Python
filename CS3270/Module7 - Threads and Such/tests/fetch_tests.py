import unittest
import asyncio
import aiofiles
import os
from src import data_fetching

class TestDataFetcher(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        """Set up the DataFetcher instance for tests."""
        self.file_path = "../AustraliaWeatherData/Weather Training Data.csv"
        self.data_fetcher = data_fetching.DataFetcher(self.file_path)

    def test_chunk_size(self):
        """Test if the chunk size is correctly initialized."""
        self.assertEqual(self.data_fetcher.chunk_size, 1000)

    async def test_reading_to_chunks(self):
        """Test if the CSV is read correctly in chunks."""
        chunks = []
        async for chunk in self.data_fetcher.read_csv_in_chunks():
            chunks.append(chunk)

        self.assertGreater(len(chunks), 0, "No chunks were yielded.")

        # Validate the size of the first chunk
        self.assertLessEqual(len(chunks[0]), 1000, "Chunk size exceeds 1000 rows.")

        # Validate that each chunk is a list of dictionaries
        for chunk in chunks:
            self.assertIsInstance(chunk, list, "Chunk should be a list.")
            for row in chunk:
                self.assertIsInstance(row, dict, "Each row should be a dictionary.")

if __name__ == "__main__":
    unittest.main()
