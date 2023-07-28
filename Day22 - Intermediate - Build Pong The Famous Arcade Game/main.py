from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

import time

screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("black")
screen.tracer(0)


player_paddle = Paddle(-550)
player_score = Scoreboard("player")

computer_paddle = Paddle(550)
computer_score = Scoreboard("computer")
computer_paddle.move_value = 20



screen.update()
screen.listen()
isGameOver = False
ball = Ball()
division_line = Turtle()
division_line.hideturtle()
division_line.pencolor("white")
division_line.pensize(5)
division_line.setheading(90)



def move_computer_paddle():
    if computer_paddle.is_going_up():
        if computer_paddle.head.ycor() < 360:
            computer_paddle.paddle_move_up()
        else:
            computer_paddle.direction = "Down"
    else: 
        if computer_paddle.tail.ycor() > -342:
            computer_paddle.paddle_move_down()
        else:
            computer_paddle.direction = "Up"

def divide_board():
    division_line.penup()
    division_line.goto(0, -400)
    division_line.pendown()
    while division_line.ycor() <= 400:
        division_line.forward(30)
        division_line.penup()
        division_line.forward(30)
        division_line.pendown()

screen.onkey(key="Up", fun=player_paddle.paddle_move_up)
screen.onkey(key="Down", fun=player_paddle.paddle_move_down)
divide_board()
position = [180, 0, 150, 45, 300, 200]
while not(isGameOver):
    move_computer_paddle()
    ball.move(player_paddle=player_paddle, computer_paddle=computer_paddle)
    
    if ball.xcor() < -600:
        ball.goto(0, 0)
        computer_score.update_score()
 
        screen.update()
        time.sleep(3)
    elif ball.xcor() > 600:
        ball.goto(0, 0)
        player_score.update_score()
        
        screen.update()
        time.sleep(3)


    time.sleep(0.1)
    screen.update()

  
    

    

screen.exitonclick()