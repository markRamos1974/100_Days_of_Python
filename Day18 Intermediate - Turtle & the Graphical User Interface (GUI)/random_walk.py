from turtle import Turtle, Screen
import turtle as t
import random

my_turtle = Turtle()
screen = Screen()
t.colormode(255)




# Random Walk
def turtle_out_of_bounds(x_pos, y_pos):
    global my_turtle
    x_bound = 380
    y_bound = 320
    return (x_pos > x_bound or x_pos < -380) or (y_pos > y_bound or y_pos < -320)

def move(direction):
    global my_turtle, colors

    if direction == "left":
        my_turtle.left(90)
    else:
        my_turtle.right(90)

    my_turtle.pencolor(random_color())
    my_turtle.forward(50)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


turns_available = ["left", "right"]
my_turtle.speed(0)
my_turtle.pensize(10)

while True:
    x =  my_turtle.xcor()
    y = my_turtle.ycor()
    if not(turtle_out_of_bounds(x, y)):
        random_turn = random.choice(turns_available)
        move(random_turn)
    else:
        my_turtle.penup()
        my_turtle.goto(random.randint(-380, 380), random.randint(-320, 320))
        my_turtle.pendown()
        

