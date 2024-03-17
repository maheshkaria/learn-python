import pandas as pd

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(df["Primary Fur Color"].value_counts().to_csv("fur_count.csv"))