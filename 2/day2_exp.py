# Data types
# Python offers different primitive data types such string, float, int, boolean etc

print(type("random"))                   # it will show type str aka string
print(type(123))                        # it will show type int aka integer
print(type(123.001))                    # it will show type float
print(type(True))                       # it will show type bool

# Function is something helps to run same code again and again by calling them with distinct name
# print(), len() and type() all of them are some examples of function which we have used so far

a = 123
print("value of a: " + str(a))  # we can type cast variable from any data type to any other data type as shown

# math operations
# + -> adds inputs
# - -> subtract inputs
# * -> multiple inputs
# / -> divides number
# % -> divides number and return remainder
# ** -> power operator
# PEDMAS order is followed from left to right

a = 123

a += 1          # a = a + 1 can be re-written as a += 1
a -= 1          # a = a - 1 can be re-written as a -= 1 and is applicable to multiplication and division as well

# f-strings if you want to print you have to convert data type to string to avoid type conversion we can use f-strings
print(f"random number {a}")

