from turtle import Turtle, Screen
from random import randint, choice


scr = Screen()
scr.setup(width=500, height=400)

color = ["red", "yellow", "green", "blue", "orange", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
turtle_list = []
user_bat = scr.textinput(title="Make your bet", prompt="Which turtle will win the race? enter a colour: ")
print(f"{user_bat}")

for _ in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(color[_])
    tim.penup()
    tim.goto(x=-240, y=y_pos[_])
    turtle_list.append(tim)

is_race_on = False

if user_bat:
    is_race_on = True


while is_race_on:
    rand_dist = randint(0, 10)
    choice(turtle_list).forward(rand_dist)

    for each_turtle in turtle_list:
        if each_turtle.xcor() >= 240:
            is_race_on = False

            print(f"{each_turtle.pencolor()} won the match!")
            if user_bat == each_turtle.pencolor():
                print("you were right!")
            else:
                print("your bet was wrong!")
            break



scr.exitonclick()