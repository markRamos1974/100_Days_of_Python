from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()

        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shape("turtle")

    def move_forward(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
        else:
            self.forward(MOVE_DISTANCE)

    def move_backward(self):
        if self.ycor() != STARTING_POSITION[1]:
            self.backward(MOVE_DISTANCE)

 