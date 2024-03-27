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

