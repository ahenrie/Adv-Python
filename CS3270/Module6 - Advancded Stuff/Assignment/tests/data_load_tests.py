import unittest
import pandas as pd
from src.data_load import convert_temps, read_csv

class TestConvertTemps(unittest.TestCase):
    def setUp(self) -> None:
        self.df = read_csv("../../AustraliaWeatherData/Weather Training Data.csv")
        self.length = len(self.df.columns.tolist())

        self.df_complete = pd.DataFrame({
            'MinTemp': [10, 20, 30],
            'MaxTemp': [15, 25, 35],
            'Temp9am': [12, 22, 32],
            'Temp3pm': [14, 24, 34]
        })

    # Test new columns are being added.
    def test_new_columns(self):
        convert_temps(self.df)
        self.assertGreater(len(self.df.columns.tolist()), self.length)

    def test_convert_temps_complete(self):
        """Test conversion with complete data."""
        convert_temps(self.df_complete)
        self.assertEqual(self.df_complete['MinTemp_F'].tolist(), [50.0, 68.0, 86.0])
        self.assertEqual(self.df_complete['MaxTemp_F'].tolist(), [59.0, 77.0, 95.0])
        self.assertEqual(self.df_complete['Temp9am_F'].tolist(), [53.6, 71.6, 89.6])
        self.assertEqual(self.df_complete['Temp3pm_F'].tolist(), [57.2, 75.2, 93.2])

    def test_temp_conversions(self):
        """Test individual temperature conversions while handling nulls."""
        # Apply conversion to the DataFrame
        convert_temps(self.df)

        # Check that each conversion is correct
        for index, row in self.df.iterrows():
            # Check if MaxTemp is not null
            if pd.notnull(row['MaxTemp']):
                expected_max_f = row['MaxTemp'] * 9/5 + 32
                self.assertAlmostEqual(row['MaxTemp_F'], expected_max_f, places=2)

            # Check if MinTemp is not null
            if pd.notnull(row['MinTemp']):
                expected_min_f = row['MinTemp'] * 9/5 + 32
                self.assertAlmostEqual(row['MinTemp_F'], expected_min_f, places=2)

            # Check if Temp9am is not null
            if pd.notnull(row['Temp9am']):
                expected_temp9am_f = row['Temp9am'] * 9/5 + 32
                self.assertAlmostEqual(row['Temp9am_F'], expected_temp9am_f, places=2)

            # Check if Temp3pm is not null
            if pd.notnull(row['Temp3pm']):
                expected_temp3pm_f = row['Temp3pm'] * 9/5 + 32
                self.assertAlmostEqual(row['Temp3pm_F'], expected_temp3pm_f, places=2)


if __name__ == '__main__':
    unittest.main()
