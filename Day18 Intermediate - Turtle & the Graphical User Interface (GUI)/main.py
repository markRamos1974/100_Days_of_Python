from turtle import Turtle, Screen
import turtle as t
import colorgram
import random

my_turtle = Turtle()
screen = Screen()
screen.setup(700, 700)
t.colormode(255)
color_object = colorgram.extract("MillionDollarPainting.jpg", 25)
colors = []
for obj in color_object:
    r = obj.rgb.r
    g = obj.rgb.g
    b = obj.rgb.b

    colors.append((r, g, b))

x_pos = -300
y_pos = -300
my_turtle.hideturtle()
my_turtle.penup()


for _ in range(8):
    my_turtle.goto(x_pos, y_pos)

    for _ in range(7):
        my_turtle.pendown()
        my_turtle.dot(25, random.choice(colors))
        my_turtle.penup()
        my_turtle.forward(100) 
    
    my_turtle.penup()

    y_pos += 100


screen.exitonclick()

