from turtle import Turtle, Screen, colormode
from random import randint, choice
t = Turtle()
colormode(255)
t.speed(100)

step_size = randint(0, 20)

while True:
    count = 2
    step_size += count
    for _ in range(0, 360, step_size):
        t.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        t.circle(step_size * count)
        t.setheading(_)
    count += 10
scr = Screen()
scr.exitonclick()
