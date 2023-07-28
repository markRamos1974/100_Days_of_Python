from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("red")
   
        self.penup()
        position = [180, 0, 150, 45, 300, 200]
        self.setheading(random.choice(position))

    def move(self, player_paddle, computer_paddle):

        
        for segments in computer_paddle.paddle_segments:
            if segments.distance(self.position()) < 20:
                if self.ycor() > 0:
                    self.setheading(180 - 45)
                else:
                    self.setheading(180 + 45)


        for segments in player_paddle.paddle_segments:
           
            if segments.distance(self.position()) < 20:
                if self.prev_x_position > self.xcor() and self.ycor() >= 0:
                
                    self.setheading(270 + 45)
       
                elif self.ycor() >= 0:
                    self.setheading(180 + 45)
                else:
                    self.setheading(45)
        
        # Right boundary
        if self.xcor() >= 600:

            if self.ycor() > 0:
                self.setheading(180 - 45)
            else:
                self.setheading(180 + 45)

        # Left boundary
        elif self.xcor() <= -600:
        
            if self.prev_x_position > self.xcor() and self.ycor() >= 0:
                
                self.setheading(270 + 45)
       
            elif self.ycor() >= 0:
                self.setheading(180 + 45)
            else:
                self.setheading(45)

        # Up boundary
        if self.ycor() >= 400:
            if self.prev_x_position < self.xcor():
                self.setheading(270 + 45)\
                
            else:
                self.setheading(180 + 45)
        
        # Down boundary
        elif self.ycor() <= -400:
            if self.prev_x_position < self.xcor():
                self.setheading(45)
            else:
                self.setheading(90 + 45)

        self.prev_x_position = self.xcor()
        self.prev_y_position = self.ycor()

        self.forward(20)


        

  
        