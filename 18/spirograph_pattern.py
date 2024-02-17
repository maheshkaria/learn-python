from turtle import Turtle, Screen, colormode
from random import randint, choice
t = Turtle()
colormode(255)
t.speed(100)


while True:
    step_size = randint(10, 20)
    for _ in range(0, 360, step_size):
        t.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        t.circle(step_size + _)
        t.setheading(_)
        t.width(randint(0, 5))
scr = Screen()
scr.exitonclick()
