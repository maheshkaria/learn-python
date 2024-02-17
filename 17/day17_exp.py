#################################################################
# In OOPs we model some real life entity to a class aka blueprint
# every class has some attributes and methods
# attributes are nothing but variables
# methods are nothing but functions related to class
#################################################################

# Following is example of class
class Car:
    color: str = ""
    name: str = ""

    def __init__(self, color, name):
        self.color = color
        self.name = name

    def print_color(self):
        print(f"color of car is {self.color}")

    def __repr__(self):
        return "color is " + self.color


# following is example of creation of object
my_car = Car("red", "model X")
print(my_car)

# how to access class variable/attribute ?
print(my_car.color)

# how to access method ?
my_car.print_color()
