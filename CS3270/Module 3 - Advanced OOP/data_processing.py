class DataProcessor:
    def __init__(self, df) -> None:
        self.df = df
        self.process_data_frame()

    def get_df_info(self):
        info = self.df.info()
        return info

    def average_min_temp(self):
        average_mt = self.df['MinTemp'].mean().round(2)
        return average_mt

    def median_max_temp(self):
        median_temp = self.df['MaxTemp'].mean().round(2)
        return median_temp

    def mode_max_temp(self):
        mode_max = self.df['MaxTemp'].mode().round(2)

    def process_data_frame(self):
        print("Info regarding your weather CSV:")
        print("\n********************* Temperature Metrics *********************")
        print(f"Average minimum temperature: {self.average_min_temp()} °C")
        print(f"Average maximum temperature: {self.median_max_temp()} °C")
        print(f"Mode maximum temperature: {self.mode_max_temp()} °C")
        print("\n********************* Column Information **********************")
        print(self.get_df_info())
