import pandas as pd

def impute_with_mean(df, column):
    # Your code here
    # Impute missing values in 'age' column with the mean
    df_filled_mean = df.copy()
    df_filled_mean["score"] = df_filled_mean["score"].fillna(df_filled_mean["score"].mean())
    return df_filled_mean

# Example usage:
data = {
    "id": [1, 2, 3, 4, 5],
    "score": [85, None, 78, None, 92]
}
df = pd.DataFrame(data)
df_imputed = impute_with_mean(df, "score")
print(df_imputed)
