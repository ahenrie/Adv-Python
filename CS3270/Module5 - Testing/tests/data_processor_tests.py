import unittest
from unittest.mock import patch
import pandas as pd
from src.data_processing import DataProcessor

class DataProcessorTestSuite(unittest.TestCase):
    def setUp(self):
        # Sample data for testing
        data = {
            'MinTemp': [10, 12, 15, 14, 11],
            'MaxTemp': [20, 22, 24, 23, 21]
        }
        self.df = pd.DataFrame(data)
        self.processor = DataProcessor(self.df)
        print(self.df.info())

    def test_average_min_temp(self):
        """Test the average minimum temperature calculation."""
        expected_avg = 12.4
        self.assertAlmostEqual(self.processor.average_min_temp(), expected_avg)

    def test_median_max_temp(self):
        """Test the median maximum temperature calculation."""
        expected_median = 22.0
        self.assertAlmostEqual(self.processor.median_max_temp(), expected_median)

    def test_mode_max_temp(self):
        """Test the mode of maximum temperature calculation."""
        expected_mode = 20.0  # Adjust based on your test data
        self.assertEqual(self.processor.mode_max_temp()[0], expected_mode)

    @patch('pandas.DataFrame.info')
    def test_get_df_info(self, mock_info):
        '''Test that DataFrame info is retrieved correctly.'''
        self.processor.get_df_info()  # Call the method

        # Check that DataFrame.info() was called
        mock_info.assert_called_once()

if __name__ == '__main__':
    unittest.main()
