from turtle import Turtle, Screen

tim = Turtle()

tim.shape("arrow")
tim.color("red")

counter = 100
while True:
    tim.forward(counter)
    tim.right(90)

screen = Screen()
screen.exitonclick()
