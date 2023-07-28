
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, user):
        super().__init__()
        self.score = 0
        self.user = user.lower()
        self.set_default_position()
        self.color("white")
        self.write(f"{self.score}", move=False, align="center", font=("impact", 70, "normal"))
        self.hideturtle()
        
    
    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", move=False, align="center", font=("impact", 70, "normal"))

    def set_default_position(self):
        
        if self.user == "player":
            self.setposition(-100, 250)
        else:
            self.setposition(100, 250)
