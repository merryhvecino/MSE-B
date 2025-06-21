import pandas as pd

df = pd.read_parquet('./ACTIVITY_04MAY25/Sample_data_2.parquet')
print(f"Number of records: {df.shape[0]}")