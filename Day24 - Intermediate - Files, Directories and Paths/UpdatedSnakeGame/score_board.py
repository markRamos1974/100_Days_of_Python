from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self, player_score):
        super().__init__()

        self.color("white")
        self.shape("turtle")
        self.penup()
        self.hideturtle()
        
        with open("highscore.txt") as highscore:
            current_highscore = highscore.read()
            print(current_highscore)
            self.highscore = int(current_highscore)
        


        self.show_score(player_score)
        

    def show_score(self, player_score):
        if player_score > self.highscore:
            self.highscore = player_score
            with open("highscore.txt", mode="w") as highscore:
                highscore.write(str(self.highscore))

        self.clear()
        self.goto((0, 370))
        self.write(f"Score: {player_score}, Highscore: {self.highscore}", align="center", font=('Impact', 20, 'normal'))
    
    def show_game_over(self):
        self.goto((0, 0))
        self.write(f"Game over", align="center", font=('Impact', 20, 'normal'))
