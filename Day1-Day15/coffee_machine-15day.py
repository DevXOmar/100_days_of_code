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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def coins():
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many quarters?: "))
    total = round((quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01), 2)
    return total

def update_resources(type):
    global resources
    if resources['water'] < MENU[type]["ingredients"]["water"]:
        return 1
    elif resources['coffee'] < MENU[type]["ingredients"]["coffee"]:
        return 2
    elif type != 'espresso' and resources['milk'] < MENU[type]["ingredients"]["milk"]:
        return 3

    resources['water'] -= MENU[type]["ingredients"]["water"]
    resources['coffee'] -= MENU[type]["ingredients"]["coffee"]
    if type != 'espresso':
        resources['milk'] -= MENU[type]["ingredients"]["milk"]
def coffee(input):

    if input == 'report':
       for key,value in resources.items():
           print(f"{key} : {value}ml")
       return
    run_out = update_resources(input)
    if run_out == 1:
        print("Sorry there is not enough water.")
        return
    elif run_out == 2:
        print("Sorry there is not enough coffee.")
        return
    elif run_out == 3:
        print("Sorry there is not enough milk.")
        return
    print("Please insert coins.")
    cost = coins()

    if cost < MENU[coffee_type]['cost']:
        return 1

    change = cost - MENU[coffee_type]['cost']
    print(cost)
    print(f"Here is {change} in change.")
    print(f"Here is your {coffee_type} ☕️. Enjoy!")
turn_off = False
while not turn_off:
    coffee_type = input(" What would you like? (espresso/latte/cappuccino): ").strip().lower()
    if coffee_type == 'off':
        turn_off = True
        break
    # print(resources)
    if coffee(coffee_type) == 1:
        print("Sorry not enough money!")
    # print(resources)

