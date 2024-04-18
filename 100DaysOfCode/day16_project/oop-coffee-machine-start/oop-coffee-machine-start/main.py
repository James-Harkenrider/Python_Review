from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drink_menu = Menu()
coffee_machine = CoffeeMaker()
cash_register = MoneyMachine()

machine_active = True
missing_ingredients = []

while machine_active:
    # TODO: Ask user for drink selection
    available_drink = drink_menu.get_items()
    drink_request = input(f"Please make a drink selection. ({available_drink}): ")

    if drink_request.lower() == 'off':
        machine_active = False

    elif drink_request.lower() == 'report':
        coffee_machine.report()
        cash_register.report()

    else:
        drink_menu_object = drink_menu.find_drink(drink_request)
        can_make = coffee_machine.is_resource_sufficient(drink_menu_object)
        can_pay = True
        if can_make:
            can_pay = cash_register.make_payment(drink_menu_object.cost)

        if can_make and can_pay:
            coffee_machine.make_coffee(drink_menu_object)
