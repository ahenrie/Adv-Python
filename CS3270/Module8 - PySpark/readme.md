# Pyspark for data processing in clusters.
# Weather Data Processing with PySpark

This project utilizes PySpark to analyze weather data efficiently. It provides insights into temperature, rainfall, humidity, and other relevant metrics through various SQL queries and summary statistics.

## Requirements

To run this project, ensure you have the following installed:

- Python 3.6 or later
- Apache Spark (version 3.5.3)
- PySpark (compatible with your Spark version)
- A compatible Java Development Kit (JDK)

You can set up a virtual environment to manage dependencies effectively:

```bash
python -m venv venv
source venv/bin/activate
```

### Install Required Python Libraries

You may need additional libraries for your environment. Install them using pip:

```bash
pip install pyspark
```

## Logging Configuration

The tutorial I followed for PySpark had too much printing to the console. I changed the bash script to this to send all logging to dev/null:

```bash
#!/bin/bash
${SPARK_HOME}/bin/spark-submit \
--master local[4] \
--executor-memory 1G \
--driver-memory 1G \
--conf spark.sql.warehouse.dir="file:///tmp/spark-warehouse" \
--packages com.databricks:spark-csv_2.11:1.5.0 \
--packages com.amazonaws:aws-java-sdk-pom:1.10.34 \
--packages org.apache.hadoop:hadoop-aws:2.8.0 \
$@ 2>/dev/null
```

## Testing

Testing was very simple and straightforward. I compared different aspects of the PySpark Data Frame to a Pandas Data Frame. This is the only objected oriented part of this project.
What is compared between the Data Frames:
  1. Number of Columns
  2. Number of Rows
  3. Summations of coumns that contain numeric types

## How to Use

1. **Set the File Path**: Ensure the `file_path` variable points to your CSV data file within the script.

2. **Run the PySpark Script**: You can execute the script using the following command:

   ```bash
   ./localsparksubmit.sh your_script.py
   ```

3. **Explore the Outputs**: The script will perform the following operations:
   - Load the CSV data into a DataFrame.
   - Execute SQL queries to obtain metrics like average temperatures, unique locations, and total row counts.
   - Print a summary of the relevant statistics while excluding calculations on categorical data.

### Example Output

The output will display key statistics about the weather data, such as average minimum and maximum temperatures, rainfall averages, and humidity statistics.

```bash
+----------+
|total_rows|
+----------+
|     99516|
+----------+

+------------------+------------------+
|      avg_min_temp|      avg_max_temp|
+------------------+------------------+
|12.176265985687314|23.218513184134757|
+------------------+------------------+

+----------------+
|unique_locations|
+----------------+
|              49|
+----------------+

Summary Statistics:
count:
  MinTemp: 99073
  MaxTemp: 99286
  Rainfall: 98537
  Evaporation: 56985
  Sunshine: 52199
  WindGustSpeed: 93036
  WindSpeed9am: 98581
  WindSpeed3pm: 97681
  Humidity9am: 98283
  Humidity3pm: 97010
  Pressure9am: 89768
  Pressure3pm: 89780
  Cloud9am: 61944
  Cloud3pm: 59514
  Temp9am: 98902
  Temp3pm: 97612
mean:
```

## License
This project is licensed under the [MIT License](LICENSE).
