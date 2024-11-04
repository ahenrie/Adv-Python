import unittest
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

class TestWeatherDataProcessing(unittest.TestCase):
    """
    Unit tests for verifying the correctness of weather data processing
    using both PySpark DataFrame and Pandas DataFrame.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the Spark session and load the weather data CSV file
        into both PySpark DataFrame and Pandas DataFrame before running
        the tests.
        """
        cls.spark = SparkSession.builder \
            .appName("TestWeatherData") \
            .getOrCreate()
        cls.file_path = "/Users/based/Desktop/Programming/Python/CS3270/AustraliaWeatherData/Weather Training Data.csv"
        cls.df = cls.spark.read.csv(cls.file_path, header=True, inferSchema=True)
        cls.pd_df = pd.read_csv(cls.file_path)

    def test_rows(self):
        """
        Test that the number of rows in the PySpark DataFrame matches
        the number of rows in the Pandas DataFrame.
        """
        print("Testing the number of rows between PySpark and Pandas")
        self.assertEqual(self.df.count(), len(self.pd_df))

    def test_columns(self):
        """
        Test that the number of columns in the PySpark DataFrame matches
        the number of columns in the Pandas DataFrame.
        """
        print("Testing the number of columns between PySpark and Pandas")
        self.assertEqual(len(self.df.columns), len(self.pd_df.columns))

    def test_column_sums(self):
        """
        Test that the sum of each numeric column in the PySpark DataFrame
        matches the sum of the corresponding column in the Pandas DataFrame.
        Only numeric columns are considered for this test.
        """
        print("Testing sums of each column between PySpark and Pandas")
        for column in self.df.columns:
            # Skip non-numeric columns for sum
            if self.df.schema[column].dataType.typeName() in ['integer', 'double', 'float', 'long']:
                spark_sum = self.df.select(col(column)).agg({'*': 'sum'}).collect()[0][0]
                pandas_sum = self.pd_df[column].sum()
                self.assertAlmostEqual(spark_sum, pandas_sum, places=5,
                                       msg=f"Sum mismatch for column '{column}': PySpark sum = {spark_sum}, Pandas sum = {pandas_sum}")

    @classmethod
    def tearDownClass(cls):
        """
        Stop the Spark session after all tests have been executed.
        """
        cls.spark.stop()

if __name__ == '__main__':
    unittest.main()
