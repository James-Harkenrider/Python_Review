def report():
    """Report available resources left in the coffee machine"""
    global PROFIT
    for material in RESOURCES:
        amount = RESOURCES[material]
        if material == "Coffee":
            print(f"{material}: {amount}g")
        else:
            print(f"{material}: {amount}ml")
    print(f"profit: ${round(PROFIT, 2)}")


def user_prompt():
    """Takes in a menu with all supported drink options and prompts user to make a selection"""
    options = list(MENU.keys())
    secret_options = ['off', 'report']
    selection = input(f"What would you like? ({'/'.join(options)}): ")
    while selection.lower() not in options and selection.lower() not in secret_options:
        print(f"Sorry, {selection} is not a valid option. Please make a new selection.")
        selection = input(f"What would you like? ({'/'.join(options)}): ")
    return selection


def check_resources(drink):
    drink_ingredients = drink["ingredients"]
    ingredient_list = []
    for ingredient in drink_ingredients:
        if drink_ingredients[ingredient] > RESOURCES[ingredient]:
            ingredient_list.append(ingredient)
    if len(ingredient_list) > 0:
        return ingredient_list
    else:
        for ingredient in drink_ingredients:
            RESOURCES[ingredient] -= drink_ingredients[ingredient]
    return None


def check_money(input_coins, cost):
    money_recieved = 0
    global PROFIT
    for coin_type in MONEY:
        money_recieved += MONEY[coin_type] * input_coins[coin_type]
    change = round(money_recieved - cost, 2)
    PROFIT = money_recieved - change
    return change


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

MONEY = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}

payment = {
    "quarters": 0,
    "dimes": 0,
    "nickles": 0,
    "pennies": 0
}
PROFIT = 0
turn_off = False
while not turn_off:
    beverage = user_prompt()
    if beverage.lower() == 'off':
        turn_off = True
        continue
    elif beverage.lower() == 'report':
        report()
        continue
    enough_resources = check_resources(MENU[beverage])
    item_cost = MENU[beverage]["cost"]
    if not enough_resources:
        payment = {
            "quarters": int(input("How many quarters?: ")),
            "dimes": int(input("How many dimes?: ")),
            "nickles": int(input("How many nickles?: ")),
            "pennies": int(input("How many pennies?: "))
        }
        customer_change = check_money(payment, item_cost)
        if customer_change >= 0:
            print(f"Here is ${customer_change} in change.")
            print(f"Here is your {beverage} ☕️. Enjoy!")
        else:
            print("Sorry, that's not enough money. Money refunded.")
    else:
        print(f"Sorry, there is not enough {" or ".join(enough_resources)}.")

    payment = {
        "quarters": 0,
        "dimes": 0,
        "nickles": 0,
        "pennies": 0
    }
