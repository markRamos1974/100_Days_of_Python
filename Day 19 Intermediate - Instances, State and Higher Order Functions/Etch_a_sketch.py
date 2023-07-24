from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()

def move_forward():
    my_turtle.forward(10)

def move_backward():
    my_turtle.backward(10)

def rotate_counter_clockwise():
    current_heading = my_turtle.heading()
    my_turtle.setheading(current_heading + 10)

def rotate_clockwise():
    current_heading = my_turtle.heading()
    my_turtle.setheading(current_heading - 10)

def reset_screen():
    screen.resetscreen()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=rotate_counter_clockwise)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=reset_screen)

screen.exitonclick()