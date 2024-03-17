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
import pandas
# Pandas library helps in data analysis
# we can install pandas using 'pip install pandas'

# It supports 1-D series and 2-D dataframe data types
# Series is basically list while Dataframe is tabular representation which has row and column

import pandas as pd

df = pd.read_csv("weather_data.csv")

print(df["temp"])

print(df)

print(type(df))

print(df.to_dict())     # we can convert it to dict

print(type(df["temp"]))     # each column in pandas DF is basically Series
print(df["temp"].to_list())     # we can convert any Series object to python list using to_list()

print(df["temp"].sum()/df["temp"].count())      # average temp

print(df["temp"].mean())    # average temp using mean function

print(df["temp"].max())     # get max value

print(df["condition"])

print(df.condition)     # we can use dot notation with pandas dataframe like this

print(df[df.day == "Monday"])

print(df[df.temp == df.temp.max()])


monday_temp = df[df.day == "Monday"].temp
print((monday_temp * 9/5) + 32)


# create dataframe from scratch
data_dict = {
    "students": ["abc", "def", "ghi"],
    "scores": [21, 22, 55]
}

data_df = pandas.DataFrame(data_dict)
data_df.to_csv("new_file.csv", index=False)
print(data_df)





