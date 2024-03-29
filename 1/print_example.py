# print function is used to print string on console

print("Hello World!")

print("Hello World!\nHello World!\nHello World!")

# We can write comment using docstring for multi-line comment """""" and # for single line

"""
multi-line
comment
"""
# single line comment

# Debugging - we can attach break point to a line or function or using logger or print certain values while execution

# To concat string we can use + and concat two string

print("hello" + " " + "world")

# we can use formatter too for concat string

print(f"my string is here %s" % "random")

# variable is placeholder where we can store data/information to use it later using name of variable
# we can define variable as shown below

my_var: float = 1.0
print(my_var)

# To take input from user we can use input() and store result in some variable
# user_input = eval(input("enter a number: "))
# print(f"user has entered number: %d" % user_input)


user_input = input("enter a name: ")
print(f"name %s has %d chars" % (user_input, len(user_input)))

# variable naming convention
# it should start with alphabet or underscore
# we can use number but it can not be first char of var name
# we can not use standard keyword as variable name
# variable is case sensitive so make sure you are using same case everywhere
# standard convention is to keep small case for variable name


