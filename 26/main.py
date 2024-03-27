import random
import pandas as pd

# how to create list using list comprehensions

# list comprehension is created using another sequence such as set/list/tuple/string
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# unconditional list comprehension
new_list = [item * item for item in my_list]

print(new_list)

# conditional list comprehension
new_list = [item * item for item in my_list if item % 2 == 0]

print(new_list)

# conditional list comprehension -> print only even numbers
new_list = [item for item in my_list if item % 2 == 0]

print(new_list)

# dictionary comprehension is to create new dictionary using existing dictionary

names = ['a', 'f', 'd', 'o']

# dict comprehension example
names_dict = {new_key: random.randint(1, 100) for new_key in names}
print(names_dict)


# dict comprehension with filter
passed_names_dict = {key: val for (key, val) in names_dict.items() if val > 50}
print(passed_names_dict)

# how to iterate over pandas dataframe

student_dict = {
    "student": ["a", "b", "c"],
    "score": [45, 85, 65]
}

student_df = pd.DataFrame(student_dict)
print(student_df)

for (index, val) in student_df.iterrows():
    if val.score > 50:
        print(val.student)
        print(val.score)