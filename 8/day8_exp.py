# follwing is example of function with function input, we can have as many params in a function
def greet(name):
    print(f"line 1 {name}")
    print(f"line 2 {name}")
    print(f"line 3 {name}")

greet(name="Mahesh")

############################################################################
def greet_with(name, location):
    print(f"hello {name}")
    print(f"what it is like to live in {location}")


# when provide params in same order as function it is called as positional arguments
greet_with("mumbai", "mahesh")


# when provide keyword of param along with value as function input it is called as keyword arguments
greet_with(location="mumbai", name="mahesh")


