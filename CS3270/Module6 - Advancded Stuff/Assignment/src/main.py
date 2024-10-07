from data_load import *
from data_vis import *

def main():
    filepath = "../../AustraliaWeatherData/Weather Training Data.csv"
    df = read_csv(filepath)
    visualize_temperature_trends(df)

    # Location filtering and vis
    location_stats_df = group_by_location(df)
    visualize_location_stats(location_stats_df)

    # Filtering using lambda function
    filtered_df = filter_by_temperature(df, min_temp=15, max_temp=20)
    visualize_temperature_trends(filtered_df)

    # Filter, location, and bar chart
    create_special_chart(df, min_temp=20, max_temp=35)

if __name__ == '__main__':
    main()
