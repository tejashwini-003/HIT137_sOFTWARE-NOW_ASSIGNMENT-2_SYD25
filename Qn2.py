import os
import pandas as pd
import numpy as np

# [1] Reading files and directories in Python using os module
FOLDER = r"C:\Users\ADMIN\Desktop\SOFTWARE NOW\temperatures"

MONTHS = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]
# [4] Dictionary usage in Python to map months to seasons
SEASON_MAP = {
    "December": "Summer", "January": "Summer", "February": "Summer",
    "March": "Autumn", "April": "Autumn", "May": "Autumn",
    "June": "Winter", "July": "Winter", "August": "Winter",
    "September": "Spring", "October": "Spring", "November": "Spring"
}

def load_data():
    data_frames = []
    # [1] Reading files from a directory
    for file in os.listdir(FOLDER):
        if file.endswith(".csv"):
            path = os.path.join(FOLDER, file)

            # [2] Reading CSV files using pandas
            df = pd.read_csv(path)

            if "STATION_NAME" in df.columns:
                df = df.rename(columns={"STATION_NAME": "Station"})
            else:
                continue

            df = df[["Station"] + MONTHS]

            # [3] Reshaping CSV data without manual loops (alternative to non-pandas CSV handling)
            long_df = df.melt(
                id_vars="Station",
                value_vars=MONTHS,
                var_name="Month",
                value_name="Temp"
            )
            data_frames.append(long_df)

    if len(data_frames) == 0:
        return pd.DataFrame()

    data = pd.concat(data_frames, ignore_index=True)
    data = data.dropna(subset=["Temp"])
    return data

def add_season(data):
    # [4] Mapping values using dictionary
    data["Season"] = data["Month"].map(SEASON_MAP)
    return data

def seasonal_average(data):
    # [7] Rounding values after decimal points
    return data.groupby("Season")["Temp"].mean().round(1)

def station_ranges(data):
    stats = data.groupby("Station")["Temp"].agg(["max", "min"])
    stats["range"] = stats["max"] - stats["min"]
    max_range = stats["range"].max()
    return stats[stats["range"] == max_range]

def temperature_stability(data):
    # [8] Standard deviation calculation
    std = data.groupby("Station")["Temp"].std()
    return std[std == std.min()], std[std == std.max()]

def save_seasonal(avg):
    # [5] Printing degree Celsius using Unicode (°)

    # [6] Writing output to a text file
    
    with open("average_temp.txt", "w") as f:
        for s in ["Summer", "Autumn", "Winter", "Spring"]:
            f.write(f"{s}: {avg[s]}°C\n")

def save_ranges(stations):
    # [6] Writing formatted data to a file
    with open("largest_temp_range_station.txt", "w") as f:
        for name, row in stations.iterrows():
            f.write(
                f"Station {name}: Range {row['range']:.1f}°C "
                f"(Max: {row['max']:.1f}°C, Min: {row['min']:.1f}°C)\n"
            )

def save_stability(stable, variable):
    # [8] Writing statistical results (standard deviation) to file
    with open("temperature_stability_stations.txt", "w") as f:
        for s, v in stable.items():
            f.write(f"Most Stable: Station {s}: StdDev {v:.1f}°C\n")
        for s, v in variable.items():
            f.write(f"Most Variable: Station {s}: StdDev {v:.1f}°C\n")

def main():
    data = load_data()
    if data.empty:
        print("No data found.")
        return

    data = add_season(data)
    avg = seasonal_average(data)
    ranges = station_ranges(data)
    stable, variable = temperature_stability(data)
    save_seasonal(avg)
    save_ranges(ranges)
    save_stability(stable, variable)

    print("Processing complete.")

if __name__ == "__main__":
    main()
