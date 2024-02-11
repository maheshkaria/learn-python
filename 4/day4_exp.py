import random
# we can import standard module or user defined modules using import statement
# module is package or collection of related code

# we can generate random int using randint function
print(random.randint(1, 100))

# we can generate random float using random function
print(random.random())

######################################################################

# Python list is type of data structure which allows to keep multiple items in a list and maintains order of insertion

my_list = ["item1", "item2", "item3", 4, True, 4.05, "random string"]

print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])
print(my_list[5])
print(my_list[6])
print(my_list)
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])
print(my_list[-4])
print(my_list[-5])
print(my_list[-6])
print(my_list[-0])
# -0 or 0 is same thing
# to add item in list
my_list.append("my_new_item")
print(my_list)

my_list.extend(["extended1", "extended2"])

print(my_list)
list1 = ["l11", "l12"]
list2 = ["l21", "l22"]

# nested list example
new_l1_l2 = [list1, list2]
print(new_l1_l2)

