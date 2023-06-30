rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
#Write your code below this line 👇
hand_signals = [rock, paper, scissors]

user_choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0, 1)

print(hand_signals[user_choice])
print("Computer choose: ")
print(hand_signals[computer_choice])

if user_choice == computer_choice:
    print("It's a draw.")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif user_choice == 1 and computer_choice == 0:
    print("You Win!")
elif user_choice == 2 and computer_choice == 1:
    print("You Win!")
elif user_choice != 0 or user_choice != 1 or user_choice != 2:
    print("You Lose!")
else:
    print("You Lose!")
