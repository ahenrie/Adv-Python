# My Module with Australian Weather

This module allows for some basic functionality with Australian Weather data (csv).

## Dataset Overview

RangeIndex: 42677 entries, 0 to 42676
Data columns (total 22 columns):
| #  | Column         | Non-Null Count | Dtype   |
|----|----------------|----------------|---------|
| 0  | row ID         | 42677          | object  |
| 1  | Location       | 42677          | object  |
| 2  | MinTemp        | 42483          | float64 |
| 3  | MaxTemp        | 42585          | float64 |
| 4  | Rainfall       | 42250          | float64 |
| 5  | Evaporation    | 24365          | float64 |
| 6  | Sunshine       | 22178          | float64 |
| 7  | WindGustDir    | 39868          | object  |
| 8  | WindGustSpeed  | 39887          | float64 |
| 9  | WindDir9am     | 39670          | object  |
| 10 | WindDir3pm     | 41547          | object  |
| 11 | WindSpeed9am   | 42264          | float64 |
| 12 | WindSpeed3pm   | 41882          | float64 |
| 13 | Humidity9am    | 42136          | float64 |
| 14 | Humidity3pm    | 41573          | float64 |
| 15 | Pressure9am    | 38411          | float64 |
| 16 | Pressure3pm    | 38432          | float64 |
| 17 | Cloud9am       | 26592          | float64 |
| 18 | Cloud3pm       | 25585          | float64 |
| 19 | Temp9am        | 42387          | float64 |
| 20 | Temp3pm        | 41855          | float64 |
| 21 | RainToday      | 42250          | object  |

## Installation

```bash
pip install setuptools wheel
python setup.py sdist bdist_wheel

pip install my_module
```

## Proof of my_module Install

A successful installation should show something like this:\
```bash
(venv) based # ~/Desktop/Programming/Python/CS3270/Module2 $ pip install my_module

Collecting my_module
  Downloading my_module-1.6.2.zip (967 bytes)
  Preparing metadata (setup.py) ... done
Building wheels for collected packages: my_module
  Building wheel for my_module (setup.py) ... done
  Created wheel for my_module: filename=my_module-1.6.2-py3-none-any.whl size=1407 sha256=9a67d798f183ccc358dc13a65601fb68c9dbed228686a58d29980f2435f1fa57
  Stored in directory: /Users/based/Library/Caches/pip/wheels/1d/f7/0b/48cde93b0ab0b9f8d56aa72263fc811611df8a611a808037fe
Successfully built my_module
Installing collected packages: my_module
Successfully installed my_module-1.6.2
```

## Example Usage of Functions in my_module

```python
import my_module

# Read the CSV into a DataFrame
df = my_module.read_csv_pd('path_to_your_csv.csv')

# Get DataFrame info
my_module.get_df_info(df)

# Calculate average minimum temperature
avg_min_temp = my_module.average_min_temp(df, 'MinTemp')
print(f"Average Minimum Temperature: {avg_min_temp}")

# Calculate median maximum temperature
median_max_temp = my_module.median_max_temp(df, 'MaxTemp')
print(f"Median Maximum Temperature: {median_max_temp}")

# Get mode of the maximum temperature
mode_max_temp = my_module.mode_max_temp(df, 'MaxTemp')
print(f"Mode Maximum Temperature: {mode_max_temp}")

# Pretty print data overview and temperature metrics
my_module.pretty_print(df)
