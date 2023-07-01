from art import logo
from art import vs
import random
# from replit import clear
from game_data import data

def generate_random_data(data):
  """ Returns a set of data from the game data"""
  return random.choice(data)

def display_item(item, item_position):
  """Format the generated data and prints it in the console"""
  name = item["name"]
  description = item["description"]
  country = item["country"]
  
  print(f"{item_position}: {name}, {description}, {country}")
  
def check_higher(first_item, second_item):
  """ 
      check who has the most followers from the generated data.
      It returns "A" if the first data has the most followers      
      otherwise it returns "B" 
  """
  first_item_count = first_item["follower_count"]
  second_item_count = second_item["follower_count"]
  
  if  first_item_count > second_item_count:
     return "A"
  return "B"

player_score = 0
first_item = generate_random_data(data)
second_item = generate_random_data(data)
is_game_over = False

while not is_game_over:
  higher = check_higher(first_item, second_item)
  
  print(logo)
  if player_score > 0:
    print(f"You're right! Current score: {player_score}")
  display_item(first_item, "Compare A")
  print(vs)
  display_item(second_item, "Againts B")
  
  user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()
  
  # if the user got the corrent answer
  if higher == user_answer:
    player_score += 1
    first_item = second_item
    second_item = generate_random_data(data)
    # clear()
    
  # If the user got the wrong answer then the game is over then display the game result
  else:
    is_game_over = True
    # clear()
    print(logo)
    print(f"Sorry that's wrong, Final score: {player_score}")



  
  
  