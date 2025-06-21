
import pandas as pd

df = pd.read_csv('./ACTIVITY_04MAY25/sample_text.txt', header=None)
print(f"First line: {df.iloc[0,0]}")
print(f"Last line: {df.iloc[-1,0]}") # -1 is shorthand for the last row, 0 is the first column