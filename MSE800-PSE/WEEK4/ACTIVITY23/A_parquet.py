import pandas as pd

file_name = 'ACTIVITY23\Sample_data_2.parquet'

# Read the Parquet file
df = pd.read_parquet(file_name)

# Print number of records
print("Number of records in the file:", len(df))