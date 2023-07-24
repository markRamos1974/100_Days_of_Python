from turtle import Turtle, Screen
import random
import turtle




screen = Screen()
screen.setup(500, 500)

starting_positions = [-200, -125 , -55, 25, 100, 175]
user_bet = screen.textinput(title="Enter your bet in the turtle race", prompt="What turtle you are rooting for?")
colors = ["red", "blue", "green", "yellow", "violet", "purple", "orange"]
my_turtles = []
is_race_on = False

for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=(-200), y=starting_positions[index])
    my_turtles.append(new_turtle)

if user_bet in colors:
    is_race_on = True

while is_race_on: 
    for my_turtle in my_turtles:
        random_pace = random.randint(0, 10)
        my_turtle.forward(random_pace)

        if my_turtle.xcor() >= 200:
            print("There is a winner")
            is_race_on = False

            if my_turtle.color()[0].lower() == user_bet.lower():
                print(f"You win")
            else:
                print(f"You lose")

            print(f"turtle {my_turtle.color()[0]} finished the race first")





screen.exitonclick()