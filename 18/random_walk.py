from turtle import Turtle, Screen, colormode
from random import randint
t = Turtle()
colormode(255)
t.pensize(10)
t.speed(100)

while True:
    val = randint(1, 255) % 2
    t.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    if val:
        t.forward(30)
    else:
        t.backward(30)

    if val:
        t.setheading(90)
    else:
        t.setheading(180)



scr = Screen()
scr.exitonclick()
