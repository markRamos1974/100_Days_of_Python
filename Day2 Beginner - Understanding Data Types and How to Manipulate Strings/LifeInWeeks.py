# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age = int(age)
age_cap = 90
days_in_year = 365
weeks_in_year = 52 
months_in_year  = 12

total_days_in_year = days_in_year * age_cap
total_weeks_in_year = weeks_in_year * age_cap
total_months_in_year = months_in_year * age_cap

user_days_in_year = days_in_year * age
user_weeks_in_year = weeks_in_year * age
user_months_in_year = months_in_year * age

user_total_days_in_year = total_days_in_year - user_days_in_year
user_total_weeks_in_year = total_weeks_in_year - user_weeks_in_year
user_total_months_in_year = total_months_in_year - user_months_in_year

print(f"You have {user_total_days_in_year } days, {user_total_weeks_in_year} weeks, and {user_total_months_in_year} months left.")




