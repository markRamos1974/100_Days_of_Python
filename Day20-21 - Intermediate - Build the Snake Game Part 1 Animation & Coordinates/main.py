from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=800) #Boundary is 680
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
snake_food = Food()

screen.update()
screen.listen()

def move_up():
    snake.head.setheading(90)
def move_down():
    snake.head.setheading(270)
def turn_right():
    snake.head.setheading(0)
def turn_left():
    snake.head.setheading(180)

speed = [0.07, 0.05, 0.03, 0.02, 0.01]
speed_index = 0
isGameOver = False
player_score = 0

score_tracker = ScoreBoard(player_score=player_score)
while not(isGameOver):
    snake.move()
    if snake_food.distance(snake.head.position()) < 20:
        snake_food.place_random()
        player_score += 1
        snake.add_snake_segment()
        score_tracker.show_score(player_score=player_score)
        if player_score % 5 == 0 and player_score != 0 and speed_index != 3:
            speed_index += 1



    screen.update()
  
    
    time.sleep(speed[speed_index])

    for segment in snake.snake_segments:
        if segment != snake.head:
            if snake.head.distance(segment.position()) < 1:
                isGameOver = True

    if snake.head.xcor() >= 390 or snake.head.xcor() <= -390:
        isGameOver = True
    if snake.head.ycor() >= 390 or snake.head.ycor() <= -390:
        isGameOver = True
 

    # Manage controls
    snake_heading = snake.head.heading()
    if snake_heading == 0 or snake_heading == 180:
        screen.onkey(key="Up", fun=move_up)
        screen.onkey(key="Down", fun=move_down)

        if snake_heading == 0:
            screen.onkey(key="Right", fun=move_down)
            screen.onkey(key="Left", fun=move_up)
        
        else:
            screen.onkey(key="Right", fun=move_up)
            screen.onkey(key="Left", fun=move_down)


    elif snake_heading == 90 or snake_heading == 270:
        screen.onkey(key="Right", fun=turn_right)
        screen.onkey(key="Left", fun=turn_left)

        screen.onkey(key="Up", fun=None)
        screen.onkey(key="Down", fun=None)
        
        
score_tracker.show_game_over()

    


screen.exitonclick()
