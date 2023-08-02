# list_of_names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in list_of_names if len(name) < 5]
# long_names = [name.upper() for name in list_of_names if len(name) >= 5]
# print(long_names)

import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(key, value)

dataframe = pandas.DataFrame(student_dict)
# print(dataframe)

for (index, data) in dataframe.iterrows():
    print(f"{data.score} \n")

