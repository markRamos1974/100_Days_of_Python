import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

random_word = random.choice(word_list)
print(random_word)
player_lives = 6
# setups the underlined word display


hidden_word = []
def word_display(chosen_word):
    global hidden_word
    for _ in range(len(chosen_word)):
        hidden_word.append("_")
    display_hidden_state(hidden_word)



# Update underlined display on user guess
def update_word(user_guess):
    global hidden_word, random_word
    # replace every "_" with corresponding letter from user_guess
    for index in range(len(random_word)):
        if user_guess == random_word[index]:
            hidden_word[index] = user_guess
    display_hidden_state(hidden_word)



def display_hidden_state(hidden_word):
    display = ""
    for item in hidden_word:
        display += item
    print(f"HIDDEN WORD: {display}")



def is_letter_present(user_guess):
    global random_word
    return user_guess in random_word



def check_if_winner():
    global hidden_word
    if "_" in hidden_word:
        return False
    else: 
        return True
    


print(logo)
word_display(random_word)

while player_lives != 0:
    user_guess = input("Guess a letter: ")
    if len(user_guess) > 1:
        print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
        print("░░YOU CAN ONLY GUESS ONE WORD AT A TIME░░")
        print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
        continue
    elif is_letter_present(user_guess):
        update_word(user_guess)
       
    else:
        player_lives -= 1
        print(stages[player_lives])
        display_hidden_state(hidden_word)

    if check_if_winner():
        print("You Win")
        break
    
if player_lives == 0:
    print("You lose")