from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self, player_score):
        super().__init__()

        self.color("white")
        self.shape("turtle")
        self.penup()
        self.hideturtle()
        self.show_score(player_score)

    def show_score(self, player_score):
        self.clear()
        self.goto((0, 370))
        self.write(f"Score: {player_score}", align="center", font=('Impact', 20, 'normal'))
    
    def show_game_over(self):
        self.goto((0, 0))
        self.write(f"Game over", align="center", font=('Impact', 20, 'normal'))
