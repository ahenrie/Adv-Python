file_path = "../AustraliaWeatherData/Weather Test Data.csv"
import my_module

def main():
    df = my_module.read_csv_pd(file_path)
    print("************ Testing get_df_info and pretty_print Functions in Module ************")
    my_module.pretty_print(df)

    print("\n********************* Testing Math Functions in Module *********************")
    print(f"Testing the min temp average in module: {my_module.average_min_temp(df, 'MinTemp')}")
    print(f"Testing the max temp median in module: {my_module.median_max_temp(df, 'MinTemp')}")
    print(f"Testing the max temp mode in module: {my_module.mode_max_temp(df, 'MaxTemp')}')")

if __name__ == "__main__":
    main()
