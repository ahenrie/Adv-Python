import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from src.data_storage import DataStorage

class DataStorageTestSuite(unittest.TestCase):
    def setUp(self):
        # Sample data for testing
        data = {
            'MinTemp': [10, 12, 15],
            'MaxTemp': [20, 22, 25]
        }
        self.df = pd.DataFrame(data)
        self.storage = DataStorage(self.df)

    @patch('builtins.input', side_effect=['test_path', 'CSV'])
    @patch('pandas.DataFrame.to_csv')
    def test_get_file_type_csv(self, mock_to_csv, mock_input):
        '''Test saving the DataFrame as CSV.'''
        self.storage.get_file_type()

        # Check that the DataFrame's to_csv method was called with the correct parameters
        mock_to_csv.assert_called_once_with('test_path.csv', index=False)
        self.assertEqual(self.storage.out_file_path, 'test_path.csv')

    @patch('builtins.input', side_effect=['test_path', 'XLSX'])
    @patch('pandas.DataFrame.to_excel')
    def test_get_file_type_xlsx(self, mock_to_excel, mock_input):
        '''Test saving the DataFrame as Excel file.'''
        self.storage.get_file_type()

        # Check that the DataFrame's to_excel method was called with the correct parameters
        mock_to_excel.assert_called_once_with('test_path.xlsx', index=False)
        self.assertEqual(self.storage.out_file_path, 'test_path.xlsx')

    @patch('builtins.input', side_effect=['test_path', 'JSON'])
    @patch('pandas.DataFrame.to_json')
    def test_get_file_type_json(self, mock_to_json, mock_input):
        '''Test saving the DataFrame as JSON.'''
        self.storage.get_file_type()

        # Check that the DataFrame's to_json method was called with the correct parameters
        mock_to_json.assert_called_once_with('test_path.json', orient='records')
        self.assertEqual(self.storage.out_file_path, 'test_path.json')

if __name__ == '__main__':
    unittest.main()
