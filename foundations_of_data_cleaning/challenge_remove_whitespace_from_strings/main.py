import pandas as pd

def strip_whitespace(df):
    # Your code here
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip()
    return df

data = {
    "Fruit": [" apple", "banana ", "  cherry ", "date"],
    "Color": [" red", "yellow ", " red ", "brown"],
    "Count": [10, 5, 7, 3]
}

df = pd.DataFrame(data)
df_copy = df.copy()
#print(df_copy)
cleaned_df = strip_whitespace(df_copy)
print(cleaned_df)
