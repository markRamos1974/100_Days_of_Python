from turtle import Turtle, Screen
from state_name import StateName
import pandas

screen = Screen()
screen.title("U.S State Game")

image = "blank_states_img.gif"
screen.addshape("blank_states_img.gif")

background_image = Turtle(shape=image)
x_data = []
y_data = []
player_score = 0
wrong_attempts = 5
states_data = pandas.read_csv("50_states.csv")
states_name = states_data["state"].to_list()


while not(wrong_attempts == 0):
    player_answer = screen.textinput(title=f"Enter your answer {player_score}/50", prompt="What is the other state's name?")
    
    if player_answer == "exit":
        break
    else:
            
        if player_answer.title() in states_name:
            name = player_answer.title()
            state_data = states_data[states_data["state"] == name]
            x_position =  int(state_data.x)
            y_position =  int(state_data.y)

            print(name, x_position, y_position)
            StateName(name, x_position, y_position)

            states_name.remove(name)
            player_score += 1

print(states_name)
to_review = pandas.DataFrame(states_name)
to_review.to_csv("to_review.csv")


screen.exitonclick()