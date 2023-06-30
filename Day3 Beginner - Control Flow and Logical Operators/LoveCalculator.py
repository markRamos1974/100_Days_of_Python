# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

T_count = name1.lower().count("t") + name2.lower().count("t")
R_count = name1.lower().count("r") + name2.lower().count("r")
U_count = name1.lower().count("u") + name2.lower().count("u")
E_count = name1.lower().count("e") + name2.lower().count("e")
TRUE_COUNT_STR  = str(T_count + R_count + U_count + E_count)

L_count = name1.lower().count("l") + name2.lower().count("l")
O_count = name1.lower().count("o") + name2.lower().count("o")
V_count = name1.lower().count("v") + name2.lower().count("v")
E_count = name1.lower().count("e") + name2.lower().count("e")
LOVE_COUNT_STR  = str(L_count + O_count + V_count + E_count)

LOVE_SCORE = int(TRUE_COUNT_STR + LOVE_COUNT_STR)

if LOVE_SCORE < 10 or LOVE_SCORE > 90:
    print(f"Your score is {LOVE_SCORE}, you go together like coke and mentos.")
elif LOVE_SCORE > 40 and LOVE_SCORE < 50:
    print(f"Your score is {LOVE_SCORE}, you are alright together.")
else:
    print(f"Your score is {LOVE_SCORE}.")

