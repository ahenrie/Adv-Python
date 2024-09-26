import unittest
import types
import pandas as pd
from src.data_load import DataLoader

class DataLoaderTestSuite(unittest.TestCase):
    def setUp(self):
        self.DataLoader_test = DataLoader("../AustraliaWeatherData/Weather Test Data.csv")

    def test_init(self):
        '''Test the initialization of a DataLoader instance.'''
        self.assertIsInstance(self.DataLoader_test, DataLoader)
        self.assertGreater(len(self.DataLoader_test._chunks), 0)
        self.assertGreater(len(self.DataLoader_test.file_path), 0)
        self.assertGreater(self.DataLoader_test.chunk_size, 0)

    def test_chunk_reader(self):
        '''Test the reading of chunks into an iterator'''
        generator = self.DataLoader_test.read_csv_chunks()

        # Test the type
        self.assertIsInstance(generator, types.GeneratorType)

        # Test the size of each chunk except the last one
        chunks = list(generator)
        for chunk in chunks[:-1]:
            self.assertEqual(len(chunk), self.DataLoader_test.chunk_size)

        # Test the last chunk size (if it exists)
        if chunks:
            self.assertLessEqual(len(chunks[-1]), self.DataLoader_test.chunk_size)

    def test_chunk_to_df(self):
        '''Test the conversion of the chunk generator to a dataframe.'''
        mock_df = self.DataLoader_test.chunks_to_dataframe()

        # Test the df is created and the type is correct
        self.assertIsInstance(mock_df, pd.DataFrame)

        # Expected df size and shape compared
        expected_df = pd.read_csv("../AustraliaWeatherData/Weather Test Data.csv")
        self.assertEqual(len(mock_df), len(expected_df))
        self.assertEqual(len(mock_df.columns), len(expected_df.columns))

    def test_empty_csv(self):
        '''Test behavior when loading an empty CSV.'''
        empty_loader = DataLoader("path_to_empty_csv.csv")  # Point to a known empty CSV
        empty_df = empty_loader.chunks_to_dataframe()

        self.assertIsInstance(empty_df, pd.DataFrame)
        self.assertTrue(empty_df.empty)

    def test_file_not_found(self):
        '''Test behavior when a non-existent file is provided.'''
        not_found_loader = DataLoader("non_existent_file.csv")  # Point to a non-existent file
        not_found_df = not_found_loader.chunks_to_dataframe()

        self.assertIsInstance(not_found_df, pd.DataFrame)
        self.assertTrue(not_found_df.empty)  # Validate it returns an empty DataFrame

if __name__ == '__main__':
    unittest.main()
