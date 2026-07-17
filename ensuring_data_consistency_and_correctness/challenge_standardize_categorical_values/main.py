import pandas as pd

def standardize_column_case(df, column_name):
    # Your code here
    df_copy = df.copy()
    df_copy[column_name] = df_copy[column_name].str.lower()
    return df_copy

data = {
    "Response": ["Yes", "no", "YES", "No", "yes", "NO", "nO", "YeS"]
}
df = pd.DataFrame(data)
result = standardize_column_case(df, "Response")
print(result)
