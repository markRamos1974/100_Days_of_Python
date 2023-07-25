from turtle import Turtle
import turtle as t
import random
class Food(Turtle):
    t.colormode(255)
    def __init__(self):
        super().__init__()
        colors = ["red", "blue", "green"]
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color(random.choice(colors))
        self.penup()
        self.speed(0)
    
        self.place_random()


    def place_random(self):
        x_position = random.randint(-350, 350)
        y_position = random.randint(-350, 350)
        self.setposition(x_position, y_position)
    
                         