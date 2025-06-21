
import pandas as pd

def count_records_in_parquet(WEEK4\ACTIVITY_04MAY25\Sample_data_2.parquet):
    try:
    
        df = pd.read_parquet(WEEK4\ACTIVITY_04MAY25\Sample_data_2.parquet)
        
       
        num_records = len(df)
        print(f"Number of records in the Parquet file: {num_records}")
    except Exception as e:
        print("An error occurred while reading the Parquet file:")
        print(e)

if __name__ == "__main__":
    # Specify the path to your Parquet file
    file_path = "Sample_data_2.parquet"  # Change this if your file is in a different location
    count_records_in_parquet(file_path)
