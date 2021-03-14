from turtle import Turtle, Screen
import random

WIDHT = 500
HEIGHT = 400
screen = Screen()
screen.setup(WIDHT, HEIGHT)
colors = ["red", "blue", "black", "yellow", "orange", "green"]
user_guess = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the colors : ")
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []
is_race_on = False

if user_guess not in colors:
    print(screen.textinput(title="Invalid choice", prompt=f"Choose one of these {colors}"))
elif user_guess:
    is_race_on = True

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 240:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"You've won. The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
