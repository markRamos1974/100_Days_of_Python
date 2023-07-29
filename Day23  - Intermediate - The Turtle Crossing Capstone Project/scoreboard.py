from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.pencolor("Black")
        self.goto(-260, 250)

        self.write("Your Level: 1", align="center", font=FONT)
    
    def update(self, score):
        self.clear()
        self.write(f"Your Level: {score}", align="center", font=FONT)
