# import csv
#
# with open("weather_data.csv") as input_file:
#     data = csv.reader(input_file)
#     temperature = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
#     print(temperature)
#


# Pandas library helps in data analysis
# we can install pandas using 'pip install pandas'

# It supports 1-D series and 2-D dataframe data types
# Series is basically list while Dataframe is tabular representation which has row and column


import pandas as pd

df = pd.read_csv("weather_data.csv")
print(df["temp"])
print(df)
print(type(df))