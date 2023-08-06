fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError as err_message:
        print("Fruit pie")
    else:

        print(f"{fruits[index]} pie")


make_pie(5)