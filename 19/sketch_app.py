from turtle import Turtle, Screen

tim = Turtle()
scr = Screen()


def move_forwards():
    tim.forward(20)


def move_backwards():
    tim.backward(20)


def clear_screen():
    tim.reset()


def move_clockwise():
    for _ in range(20):
        tim.setheading(tim.heading() + 1)
        tim.forward(1)


def move_anti_clockwise():
    for _ in range(20):
        tim.setheading(tim.heading() - 1)
        tim.forward(1)


scr.listen()
scr.onkey(key="W", fun=move_forwards)
scr.onkey(key="S", fun=move_backwards)
scr.onkey(key="A", fun=move_clockwise)
scr.onkey(key="D", fun=move_anti_clockwise)
scr.onkey(key="C", fun=clear_screen)

scr.exitonclick()
