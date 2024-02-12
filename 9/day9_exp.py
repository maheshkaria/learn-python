# dictionary is a pair of key-value pair, we can define dictionary between curly braces and every key must be unique
#
my_dict = {
    "t1": "t1 data",
    "t2": "t2 data",
    "t3": "t3 data"
}


# to access data from dict we can use following
print(my_dict["t1"])
print(my_dict["t2"])
print(my_dict["t3"])

# add element to dict
my_dict["t4"] = "jkijkl"


print(my_dict.keys())   # prints all the keys

for item in my_dict:    # prints all the keys
    print(item)
    print(my_dict[item])