from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_obj = Menu()
coffee_m_obj = CoffeeMaker()
money_machine_obj = MoneyMachine()
turn_off = False
while not turn_off:
    coffee_type = input(" What would you like? (espresso/latte/cappuccino): ").strip().lower()
    if coffee_type == 'report':
        coffee_m_obj.report()
        continue
    if coffee_type == 'off':
        turn_off = True
        break
    drink = menu_obj.find_drink(coffee_type)
    current_cost = 0

    if drink:
        for item in menu_obj.menu:
            if item.name == drink.name:
                print("It's cost is ",item.cost,"$")
                current_cost = item.cost
                list1 = item

                break
    else:
         print("Drink not available.")
    if not coffee_m_obj.is_resource_sufficient(list1):
        continue
    money_machine_obj.make_payment(current_cost)
    coffee_m_obj.make_coffee(list1)
# print(type(list1))
