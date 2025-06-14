
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_resources = CoffeeMaker()
my_money_machine = MoneyMachine()
menu = Menu()

machine_is_on = True

while machine_is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        machine_is_on = False
    elif choice == "report":
        coffee_resources.report()
        my_money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_resources.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            coffee_resources.make_coffee(drink)
