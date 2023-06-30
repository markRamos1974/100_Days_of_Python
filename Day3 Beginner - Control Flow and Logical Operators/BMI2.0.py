# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = weight / height ** 2
BMI_INTEGER_VALUE = round(BMI)

if BMI < 18.5:
    print(f"Your BMI is {BMI_INTEGER_VALUE}, you are underweight.")
elif BMI > 18.5 and BMI < 25:
    print(f"Your BMI is {BMI_INTEGER_VALUE}, you have a normal weight.")
elif BMI > 25 and BMI < 30:
    print(f"Your BMI is {BMI_INTEGER_VALUE}, you are slightly overweight.")
elif BMI > 30 and BMI < 35:
     print(f"Your BMI is {BMI_INTEGER_VALUE}, you are obese.")
else:
    print(f"Your BMI is {BMI_INTEGER_VALUE}, you are clinically obese.")