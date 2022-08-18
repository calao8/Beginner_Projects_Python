from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

is_on = True

while is_on:
    
    user_choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    # user_choice can be maintainers = enter "off" to turn off the coffee machine
    
    if user_choice == "off":
        is_on = False
    elif user_choice == "report": #employees to checkup on resources
        coffeeMaker.report()
        moneyMachine.report()
    elif user_choice in menu.get_items():
        drink = menu.find_drink(user_choice)
        #check for sufficient resources for requested drink
        if coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            coffeeMaker.make_coffee(drink)
    else:
        print("Invalid Input, please try again. ")
