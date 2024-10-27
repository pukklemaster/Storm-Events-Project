# Import Packages & Assign Aliases
import os
import pandas as pd

# Designate Directory with CSVs
csv_dir = "csv_files"

# Initialise Empty Lists
details_files = []
fatalities_files = []
locations_files = []

# Loop through each file
for csv_file in os.listdir(csv_dir):
    # Check if the chosen file is a .csv
    if csv_file.endswith(".csv"):
        # Assign a file path for the csv location
        file_path = os.path.join(csv_dir, csv_file)
        
        # Read in and store the csv in a DataFrame object
        df = pd.read_csv(file_path)
        
        # Sort the DataFrame into the appropriate list
        if 'details' in csv_file.lower():
            details_files.append(df)
        elif 'fatalities' in csv_file.lower():
            fatalities_files.append(df)
        elif 'locations' in csv_file.lower():
            locations_files.append(df)

# Check if the details files have been read & stored
if details_files:
    # Concatenate DataFrames in the list, write as a combined CSV, and print a success message
    all_details = pd.concat(details_files)
    all_details.to_csv("all_details.csv", index=False)
    print("All details files concatenated into all_details.csv")

# Check if the fatalities files have been read & stored
if fatalities_files:
    # Concatenate DataFrames in the list, write as a combined CSV, and print a success message
    all_fatalities = pd.concat(fatalities_files)
    all_fatalities.to_csv("all_fatalities.csv", index=False)
    print("All fatalities files concatenated into all_fatalities.csv")

# Check if the locations files have been read & stored
if locations_files:
    # Concatenate DataFrames in the list, write as a combined CSV, and print a success message
    all_locations = pd.concat(locations_files)
    all_locations.to_csv("all_locations.csv", index=False)
    print("All locations files concatenated into all_locations.csv")