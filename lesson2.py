import pandas as pd

df = pd.read_csv("survey.csv")
print(df)
print("missing per column:")
print(df.isnull().sum())

df_clean = df.dropna()
print("cleaned:")
print(df_clean)
print(df_clean.groupby("group")["score"].mean())
