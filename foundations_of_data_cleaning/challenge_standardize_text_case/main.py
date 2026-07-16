import pandas as pd

def standardize_column_lowercase(df, column_name):
    # Your code here
    df_copy = df.copy()
    df_copy = df.copy()
    for col in df_copy.select_dtypes(include="object").columns:
        if col == column_name:
            df_copy[col] = df_copy[col].str.lower()
    return df_copy

data = {
    "fruit": ["Apple", "banana", "ORANGE", "apple", "Banana", "orange"],
    "quantity": [5, 3, 4, 2, 1, 6]
}
df = pd.DataFrame(data)
result = standardize_column_lowercase(df, "fruit")
print(result)
