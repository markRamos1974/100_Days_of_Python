# from art import logo
# # from replit import clear
# import random


# def generate_cards(cards):
#   number_of_default_cards = 2
#   user_card = []

#   for _ in range(number_of_default_cards):
#     random_card = random.choice(cards)
#     user_card.append(random_card)

#   return user_card


# def get_total_cards_score(deck):
#   sum_of_cards = 0
#   for card in deck:
#     sum_of_cards += card

#   return sum_of_cards


# def check_winner(player_score, computer_score):
#   if player_score == computer_score:
#     return "Push -> DRAW"
#   elif player_score > 21:
#     return "BUST you lose!"
#   elif player_score < computer_score and computer_score <= 21:
#     return "you lose!"
#   else:
#     return "You win!"
  



# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# def play_black_jack():
#   player_cards = generate_cards(cards);
#   computer_cards = generate_cards(cards);
#   player_current_score = get_total_cards_score(player_cards)
#   computer_total_score = get_total_cards_score(computer_cards)
  
#   is_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
# #   clear()
#   print(logo)
#   while is_playing == "y":
    
#     print(f"\tYour cards: {player_cards}, current score: {player_current_score}")
#     print(f"\tComputer's first card: {computer_cards[0]}")
  
#     draw_new_card = input("Type 'y' to get another card, type 'n' to pass: ")
#     if draw_new_card == "y":
#       player_new_card = random.choice(cards)
#       player_cards.append(player_new_card)
#       player_current_score = get_total_cards_score(player_cards)

#       if player_current_score > 21:
#         print(f"\tYour final hand: {player_cards}, final score: {player_current_score}")
#         print(f"\tComputer's final hand: {computer_cards}, final score: {computer_total_score}")
#         print("You went over. Computer Wins")
#         play_black_jack()
      
#       else:
#         computer_new_card = random.choice(cards)
#         computer_cards.append(computer_new_card)
#         computer_total_score = get_total_cards_score(computer_cards)
#     else:
#         print(f"\tYour final hand: {player_cards}, final score: {player_current_score}")
#         print(f"\tComputer's final hand: {computer_cards}, final score: {computer_total_score}")
#         print(check_winner(player_current_score, computer_total_score))
#         play_black_jack()

  
#   return 
  
    

# play_black_jack()

# OPTIMIZED CODE

from art import logo
# from replit import clear
import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


def calculate_score(cards):
  user_cards = cards
  if len(cards) == 2 and sum(cards) == 21:
    return 0
  elif sum(cards) == 21:
    return 0
  elif 11 in user_cards and sum(user_cards) > 21:
    user_cards.remove(11)
    user_cards.append(1)

  return sum(user_cards)

def check_game_result(player_score, computer_score):
  if player_score == computer_score:
    return "DRAW"
  if player_score == 0:
    return "BLACKJACK You Win!"
  elif computer_score == 0:
    return "Computer recieves BLACKJACK You Lose!"
  elif player_score > 21:
    return "Your score exceeds 21 BUST You lose!"
  elif computer_score > player_score:
    return "Computer score is greater than yours You lose!"
  else:
    return "Congratulations You Win!"


def play_game():
  player_cards = []
  computer_cards = []


  for _ in range(2):
    player_cards.append(deal_card())
    computer_cards.append(deal_card())


  is_game_over = False
  player_score = calculate_score(player_cards)
  computer_score = calculate_score(computer_cards)
  
  
  print(logo)
  while not is_game_over:
  
    print(f"  Your cards: {player_cards}, current score: {player_score}")
    print(f"  Computer's first card: {computer_cards[0]}")
    
    if player_score == 0 or computer_score == 0 or player_score > 21:
        is_game_over = True
    else:
      
      should_draw = input("Type 'y' to get another card, type 'n' to pass: ")
      if should_draw == "y":
        player_cards.append(deal_card())
        player_score = calculate_score(player_cards)
     
      else:
        is_game_over = True
       
  while computer_score < 17 and computer_score != 0:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
    
  
  print(f"  Your final cards: {player_cards}, final score: {player_score}")
  print(f"  Computer's final cards: {computer_cards}, final score: {computer_score}")
  print(check_game_result(player_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  # clear()
  play_game()
