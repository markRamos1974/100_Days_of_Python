from turtle import Turtle

class SnakeSegment(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.hideturtle()
    
                         