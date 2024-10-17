import pandas as pd

df = pd.read_csv("../AustraliaWeatherData/Weather Training Data.csv")
unique_rain = df['RainTomorrow'].unique()
df.info()
