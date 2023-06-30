#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo
stage = {
  "easy": 10,
  "hard": 5
}

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm think a number between 1 and 100")

difficulty = input("Choose difficulty. Type 'easy' or 'hard': ").lower()

player_lives = stage[difficulty]
CORRECT_ANSWER = random.randint(1, 100)
user_guess = None
is_game_over = False

def check_answer(answer):
  global CORRECT_ANSWER
  if answer == CORRECT_ANSWER:
    print(f"The correct answer: {CORRECT_ANSWER} You win!")
    return True
  else:
    if user_guess < CORRECT_ANSWER:
         print("Too low")
    else:
      print ("Too High")
    return False
  
  

while not is_game_over:
  if player_lives == 0:
    is_game_over = True
    print("You've run out of guesses. You lose!")
  else:
      print(f"You have {player_lives} attempts remaining to guess the number.")
      user_guess = int(input("Make a guess: "))
      is_game_over = check_answer(user_guess)
      player_lives -= 1

      

      
  

  





