import pandas as pd
import numpy as np

def detect_missing(dataframe):
    # Your code here
    pass
    return dataframe.isna()
    

# Sample DataFrame for testing
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, np.nan, 30, 22],
    "City": ["New York", "Los Angeles", np.nan, "Chicago"],
    "Score": [85, 90, np.nan, 88]
}
df = pd.DataFrame(data)
print(df)
result = detect_missing(df)
print(result)
