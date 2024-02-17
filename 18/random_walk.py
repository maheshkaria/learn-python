from turtle import Turtle, Screen, colormode
from random import randint, choice
t = Turtle()
colormode(255)
t.pensize(10)
t.speed(100)

angles = [0, 90, 180, 270]

while True:
    t.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    t.forward(30)
    t.setheading(choice(angles))



scr = Screen()
scr.exitonclick()
