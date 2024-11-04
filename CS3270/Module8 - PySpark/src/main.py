from pyspark.sql import SparkSession
from pyspark.sql.utils import AnalysisException

from pyspark.sql import SparkSession
from pyspark.sql.utils import AnalysisException

def main():
    file_path = "/Users/based/Desktop/Programming/Python/CS3270/AustraliaWeatherData/Weather Training Data.csv"
    try:
        # Create a Spark session
        spark = SparkSession.builder \
            .appName("Data Processing") \
            .getOrCreate()

        # Load the CSV data into a DataFrame
        df = spark.read.csv(file_path, header=True, inferSchema=True)

        # Register the DataFrame as a temporary view
        df.createOrReplaceTempView("weather_data")

        # Execute SQL queries to analyze the data
        row_count_query = spark.sql("SELECT COUNT(*) as total_rows FROM weather_data")
        row_count_query.show()

        avg_temp_query = spark.sql("""
            SELECT AVG(MinTemp) as avg_min_temp, AVG(MaxTemp) as avg_max_temp
            FROM weather_data
        """)
        avg_temp_query.show()

        unique_locations_query = spark.sql("SELECT COUNT(DISTINCT Location) as unique_locations FROM weather_data")
        unique_locations_query.show()

        # Print summary statistics for relevant columns
        relevant_columns = [
            'MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine',
            'WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am',
            'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm',
            'Temp9am', 'Temp3pm',
        ]

        summary = df.select(relevant_columns).describe()

        # Display summary results
        summary_results = summary.collect()
        print("Summary Statistics:")
        for row in summary_results:
            print(f"{row['summary']}:")
            for col in relevant_columns:
                print(f"  {col}: {row[col]}")

    except AnalysisException as e:
        print(f"Analysis Exception: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Stop the Spark session
        spark.stop()

if __name__ == "__main__":
    main()
