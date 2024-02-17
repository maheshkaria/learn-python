from turtle import Turtle, Screen

tim = Turtle()
tim2 = Turtle()
tim3 = Turtle()

tim.shape("arrow")
tim.color("red")

counter = 100
while True:
    tim.forward(counter)
    tim.right(90)

    tim2.forward(counter)
    tim2.right(90)
    tim3.backward(counter)
    tim3.left(90)


screen = Screen()
screen.exitonclick()
