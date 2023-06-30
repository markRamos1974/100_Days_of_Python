# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_sum = 0
for height_data in student_heights:
    total_sum += height_data

average_height = total_sum / len(student_heights)

print(round(average_height))