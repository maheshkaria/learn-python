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

    """
    def __init__() is constructor which gets called as soon as object is created
    constructor is used to provide values for object initialization
    class variables are accessed using self keyword
    we can also create variables with default value example sold -> value
    """
    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.sold = False

    def print_color(self):
        print(f"color of car is {self.color}")

    def is_car_available(self):
        if not self.sold:
            print("car is available")
        else:
            print("car is not available")

    def __repr__(self):
        return "color is " + self.color


# following is example of creation of object
my_car = Car("red", "model X")
print(my_car)

# how to access class variable/attribute ?
print(my_car.color)

# how to access method ?
my_car.print_color()

my_car.is_car_available()
