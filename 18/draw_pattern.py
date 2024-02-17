from turtle import Turtle, Screen, colormode
from random import randint
t = Turtle()
colormode(255)
# t.pencolor(255, 255, 255)

for i in range(3, 11):
    angle = -360 / i
    print(f"{i}")
    t.pencolor(randint(i, 255), randint(i, 255), randint(i, 255))
    for val in range(i):

        print(f"{i}: {val}")
        t.setheading(angle * val)
        t.forward(100)


scr = Screen()
scr.exitonclick()