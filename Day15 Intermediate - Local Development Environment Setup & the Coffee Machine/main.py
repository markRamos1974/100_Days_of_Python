from menu_data import MENU
from resources_data import resources
from art import logo

def report(money):
    print("The current resource values. e.g.")
    for resource in resources:
        resource_value = resources[resource]
        print(f"{resource}: {resource_value}")
    print(f"Money: ${money}")


def prepare_drink(user_choice):
    ingredients = MENU[user_choice]["ingredients"]
    for item in ingredients:
        item_cost = ingredients[item]
        resources[item] -= item_cost


def check_resources(ingredients):
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry there is not enough {item}")
            return False
        
    return True


def process_coins(quarters, dimes, nickles, pennies, cost):
    total_quarters = quarters * 0.25
    total_dimes = dimes * 0.10
    total_nickles= nickles * 0.05
    total_pennies = pennies * 0.01

    total_payment = total_quarters + total_dimes + total_dimes + total_nickles + total_pennies
    change = total_payment - cost
    return change


money_bank = 0
is_turned_off = False


while not is_turned_off:
    print(logo)
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        is_turned_off = True
        print("Thank you for using this coffee machine thank you and goodbye")

    elif user_choice == "report":
        report(money_bank)
  
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        is_resource_sufficient = check_resources(MENU[user_choice]["ingredients"])
        if is_resource_sufficient:
            print("Pleas insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles =  int(input("how many nickles?: "))
            pennies =  int(input("how many pennies?: "))
            cost = MENU[user_choice]["cost"]
            change = round(process_coins(quarters, dimes, nickles, pennies, cost), 2)

            if change >= 0:
                prepare_drink(user_choice)
                money_bank += cost
                if change > 0:
                    print(f"Here is ${change} in change.")
                print(f"Enjoy! Here is your {user_choice}☕️.")
            else:
                print("Not enough balance please insert the amount required")
                print("Returning your money...")
    else:
        print("Invalid input please try again!")



