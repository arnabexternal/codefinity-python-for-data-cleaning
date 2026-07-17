import pandas as pd
import numpy as np

def drop_missing_rows(df):
    # Your code here
    df_dropped = df.dropna()
    return df_dropped

# Sample DataFrame for testing

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, np.nan, 30, 22],
    "city": ["New York", "Los Angeles", np.nan, "Chicago"]
}
df = pd.DataFrame(data)
result = drop_missing_rows(df)
print(result)
