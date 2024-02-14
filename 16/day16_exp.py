###############################################################
# Earlier we had procedural programming where execution used to happen sequentially but with complex problems
# there was need to better way to solve programming problems and OOPs came as one of the solution
#
# Class is nothing but logical representation of some real world entity
# and to access its attributes i.e. vars and methods, we need to object of that class.
# Object can provide access to method and variables of a class.
#
# We can create class using class keyword and following example shows creation of object.
# We can create as many objects of a given class.
# Name of class begins with Upper case as per Pascal Convention
# Name of object follows camel case
###############################################################
#
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red", "green")
#
# timmy.forward(300)
# timmy.backward(300)
# my_screen = Screen()
#
#
# print(my_screen.canvwidth)
# my_screen.exitonclick()
#
###############################################################
from prettytable import PrettyTable

pretty = PrettyTable(field_names=["field 1", "field 2"])
pretty.add_row(["my data r1", "my data again"])
pretty.add_row(["my data r2", "my data again"])
pretty.add_row(["my data r3", "my data again"])
pretty.add_autoindex("sr no")
pretty.align = "l"

print(pretty)

###############################################################

