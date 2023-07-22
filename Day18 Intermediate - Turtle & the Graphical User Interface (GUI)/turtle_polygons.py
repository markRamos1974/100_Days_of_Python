from turtle import Turtle, Screen
import random

my_turtle = Turtle()
screen = Screen()


full_turn = 360


colors = ["CadetBlue1", "chartreuse1", "cyan", "DarkMagenta", "DarkOrange", "DeepPink", "brown"]

# Polygons
my_turtle.penup()
my_turtle.goto(-100, 30)
my_turtle.pendown()
for side_count in range(3, 11):
    turn_angle = full_turn / side_count
    my_turtle.pencolor(random.choice(colors))


    for _ in range(side_count):
        my_turtle.forward(100)
        my_turtle.right(turn_angle) 
