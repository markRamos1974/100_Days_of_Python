# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
weight_intger_value = float(weight)
height_intger_value = float(height)


BMI = weight_intger_value / height_intger_value ** 2
BMI_integer_value = int(BMI)

print(BMI_integer_value)

