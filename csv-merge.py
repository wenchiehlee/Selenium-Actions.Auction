#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd

# List of file paths
file_paths = [
    "auction-utf8-filter.csv",
    "2023-utf8-filter.csv",
    "2022-utf8-filter.csv",
    "2021-utf8-filter.csv",
    "2020-utf8-filter.csv"
]

# Load and combine all CSV files
dataframes = [pd.read_csv(file) for file in file_paths]
merged_data = pd.concat(dataframes, ignore_index=True)

# Save the merged data to a new CSV file
merged_data.to_csv("2020-Now-utf8-filter.csv", index=False)

print("Data merged and saved as '2020-Now-utf8-filter.csv'")