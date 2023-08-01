from turtle import Turtle

class StateName(Turtle):

    def __init__(self, state_name, x_position, y_position):
        super().__init__()

        self.penup()
        self.hideturtle()
        self.goto(x_position, y_position)
        self.write(state_name, align="center")