import seaborn as sns
import matplotlib.pyplot as plt
from data_load import filter_by_temperature

def visualize_temperature_trends(df):
    """Visualize temperature trends using row index."""
    plt.figure(figsize=(12, 6))

    # Use the DataFrame index as x-axis
    sns.lineplot(x=df.index, y='MaxTemp', data=df, label='Max Temperature (°C)')
    sns.lineplot(x=df.index, y='MinTemp', data=df, label='Min Temperature (°C)')

    plt.title('Temperature Trends (Index-Based)')
    plt.xlabel('Index')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.tight_layout()
    plt.show()

def visualize_location_stats(location_stats_df):
    """Visualizes the average temperatures and rainfall by location."""

    # Set the style of seaborn
    sns.set(style="whitegrid")

    # Sort by MaxTemp and Rainfall in descending order
    location_stats_df = location_stats_df.sort_values(by='MaxTemp', ascending=False)

    # Create a figure and axes
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 10))

    # Plot Max and Min Temperatures
    sns.barplot(x='MaxTemp', y='Location', data=location_stats_df, ax=axes[0], palette='viridis')
    axes[0].set_title('Average Maximum Temperature by Location (°C)')
    axes[0].set_xlabel('Max Temperature (°C)')
    axes[0].set_ylabel('Location')

    # Sort by Rainfall in descending order
    location_stats_df = location_stats_df.sort_values(by='Rainfall', ascending=False)

    # Plot Rainfall
    sns.barplot(x='Rainfall', y='Location', data=location_stats_df, ax=axes[1], palette='Blues')
    axes[1].set_title('Average Rainfall by Location (mm)')
    axes[1].set_xlabel('Average Rainfall (mm)')
    axes[1].set_ylabel('Location')

    plt.tight_layout()
    plt.show()

def create_special_chart(df, min_temp=None, max_temp=None):
    # Step 1: Filter the DataFrame
    filtered_df = filter_by_temperature(df, min_temp, max_temp)

    # Step 2: Group by Location and calculate metrics
    location_stats = filtered_df.groupby('Location').agg({
        'MaxTemp': 'mean',
        'MinTemp': 'mean',
        'Rainfall': 'mean',
        'Sunshine': 'mean'
    }).reset_index()

    # Step 3: Create a bar chart
    location_stats.set_index('Location', inplace=True)
    location_stats.plot(kind='bar', figsize=(12, 6))

    plt.title('Average Weather Metrics by Location')
    plt.xlabel('Location')
    plt.ylabel('Values')
    plt.xticks(rotation=45)
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()
