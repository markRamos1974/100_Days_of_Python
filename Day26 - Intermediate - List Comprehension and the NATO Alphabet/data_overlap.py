with open("./data_overlap/file2.txt") as second_file:
    second_file_data = second_file.readlines()
    second_file_data = [int(item) for item in second_file_data]


with open("./data_overlap/file1.txt") as first_file:
    first_file_data = first_file.readlines()
    first_file_data = [int(item) for item in first_file_data]


result = [item for item in first_file_data if item in second_file_data]

# Write your code above 👆

print(result)


