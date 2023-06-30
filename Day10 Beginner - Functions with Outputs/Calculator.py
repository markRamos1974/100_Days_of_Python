from art import logo
# from replit import clear


def add_inputs(num1, num2):
    """It requires two integer input and returns the SUM of the two integer """
    return num1 + num2


def subtract_inputs(num1, num2):
    """It requires two integer input and returns the DIFFERENCE of the two integer """
    return num1 - num2


def multiply_inputs(num1, num2):
    """It requires two integer input and returns the PRODUCT of the two integer """
    return num1 * num2


def divide_inputs(num1, num2):
    """It requires two integer input and returns the QUOTIENT of the two integer """
    return num1 / num2

def raise_inputs(number, number_of_raises):
    """ Raise a number by n of times """
    return number ** number_of_raises

  
operations = {
  "+" : [add_inputs, "Addition : "],
  "-" : [subtract_inputs, "Subtraction : "],
  "*" : [multiply_inputs, "Multiplication : "],
  "/" : [divide_inputs, "Division : "],
  "**" : [raise_inputs, "Exponents : "],
}

def calculator():
  print(logo)
  first_number = float(input("What's the first number?: "))
  for operation in operations:
    print(operations[operation][1] + operation)

  should_continue = True

  while should_continue:
    operation = input("Pick an operation: ")
    next_number = float(input("What's the next number?: "))

    calculation_method = operations[operation][0]
    answer = calculation_method(first_number, next_number)
    print(f"{first_number} {operation} {next_number} = {answer}")

    should_continue_calculation = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation: ").lower()

    if should_continue_calculation == "y":
      first_number = answer
    else:
      should_continue = False
    #   clear()
      calculator()

calculator()