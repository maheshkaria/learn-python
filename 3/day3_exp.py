# Conditionals statements
# when we want to choose between 2 path we can use if-else conditionals
# we can nest if-else conditional with another if-else

##########################################

a = 10
# simple if-else
if a % 2 == 0:
    print(f"number {a} is even")
else:
    print(f"number {a} is odd")
##########################################

### nested if-else
a = 9
if a % 2 == 0:
    print(f"number {a} is even")
elif a > 10:
    print(f"number {a} greater than 10")
else:
    print(f"number {a} is neither even nor greater than 10")

##########################################

### Logical operators
# if we want to check multiple conditions in same if-else conditional then we can use logical operators
# we have 'and', 'or', 'not' logical operator

a = 10
# simple if-else
if a % 2 == 0 and a > 1:
    print(f"number {a} is even and greater than 10")
else:
    print(f"number {a} is odd")

##########################################
