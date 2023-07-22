from turtle import Turtle, Screen
import turtle as t
import random

my_turtle = Turtle()
screen = Screen()
screen.setup(600 + 4, 600 + 8)

t.colormode(255)
t.bgcolor("black")


def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

current_angle = 0
my_turtle.speed(0)
while current_angle <= 360:
    my_turtle.pencolor(generate_random_color())
    my_turtle.circle(100)
    current_angle += 5
    my_turtle.setheading(current_angle)



screen.exitonclick()