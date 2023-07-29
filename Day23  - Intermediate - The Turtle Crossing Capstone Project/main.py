import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
car = CarManager()
player = Player()
level = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.move_forward)
screen.onkey(key="Down", fun=player.move_backward)
player_level = 1

while game_is_on:
    
    time.sleep(0.1)
    screen.update()

    car.generate_car()
    car.move_forward()
  

    if player.ycor() >= 280:
        player_level += 1
        level.update(player_level)
        player.goto((0, -280))

    game_is_on = car.check_collision(player)

game_over = Turtle()
game_over.hideturtle()
game_over.write("Game Over.", align="center", font=("Courier", 24, "normal"))


screen.exitonclick()