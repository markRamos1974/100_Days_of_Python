from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

turned_off = False 


while not turned_off:
    print(logo)
    user_order = input(f"What would you like? {menu.get_items()}: ").lower()
    
    if user_order == "off":
        turned_off = True
        print("Thank you! for using our service goodbye. 🤍")
    
    elif user_order == "report":
        coffee_maker.report()
        money_machine.report()

    available_items = menu.get_items().split("/")
    if user_order in available_items and user_order != "":
        
        drink_value = menu.find_drink(user_order)
        payment_enough = money_machine.make_payment(drink_value.cost)
        can_make_drink = coffee_maker.is_resource_sufficient(drink_value)

        if payment_enough and can_make_drink:
            coffee_maker.make_coffee(drink_value)
           

