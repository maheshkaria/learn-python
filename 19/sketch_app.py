from turtle import Turtle, Screen

tim = Turtle()
scr = Screen()

def move_forwards():
    tim.forward(10)

scr.listen()
scr.onkey(key="space", fun=move_forwards)


scr.exitonclick()