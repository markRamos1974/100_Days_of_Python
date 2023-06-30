# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#If the year is can be divided by 4 cleanly
if year % 4 == 0:
    #If the year is can be divided by 100 cleanly
    if year % 100 == 0:
        #If the year is can be divided by 400 cleanly
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
