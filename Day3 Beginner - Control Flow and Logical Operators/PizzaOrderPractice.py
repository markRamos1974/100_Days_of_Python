# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_bill = 0

if size.upper() == "S":
    total_bill += 15
elif size.upper() == "M":
    total_bill += 20
else:
    total_bill += 25

if add_pepperoni.upper() == "Y":
    if size.upper() == "M" or size.upper() == "L":
        total_bill += 3
    else: 
        total_bill += 2

if extra_cheese.upper() == "Y":
    total_bill += 1


print(f"Your final bill is: ${total_bill}.")

