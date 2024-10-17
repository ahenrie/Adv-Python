import unittest
import pandas as pd
from src.data_processing import DataProcessor

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        """Set up a DataProcessor instance and sample test data."""
        self.processor = DataProcessor()
        self.test_data = [
            {'MinTemp': 10.0, 'MaxTemp': 25.0, 'RainTomorrow': '1'},
            {'MinTemp': 15.0, 'MaxTemp': 30.0, 'RainTomorrow': '0'},
            {'MinTemp': 12.0, 'MaxTemp': 28.0, 'RainTomorrow': '1'},
        ]
        self.empty_data = []

    def test_filter_rain_data(self):
        """Test that only rows where 'RainTomorrow' equals '1' are returned."""
        result = self.processor.filter_rain_data(self.test_data)
        expected = pd.DataFrame([
            {'MinTemp': 10.0, 'MaxTemp': 25.0, 'RainTomorrow': '1'},
            {'MinTemp': 12.0, 'MaxTemp': 28.0, 'RainTomorrow': '1'},
        ])
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)

    def test_filter_rain_data_empty(self):
        """Test that an empty DataFrame is returned if no rows match the filter."""
        data = [{'MinTemp': 15.0, 'MaxTemp': 30.0, 'RainTomorrow': '0'}]
        result = self.processor.filter_rain_data(data)
        self.assertTrue(result.empty)

    '''
    def test_avg_temp_data(self):
        """Test that the average temperature is calculated correctly."""
        result = self.processor.avg_temp_data(self.test_data)
        expected = pd.Series({'MinTemp': 12.333333, 'MaxTemp': 27.666667})
        pd.testing.assert_series_equal(result, expected)

    def test_process_in_parallel_empty_chunks(self):
        """Test that processing an empty list of chunks returns an empty list."""
        result = self.processor.process_in_parallel([], self.processor.avg_temp_data)
        self.assertEqual(result, [])
    '''

if __name__ == '__main__':
    unittest.main()
