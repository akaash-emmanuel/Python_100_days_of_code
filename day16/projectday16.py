from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cafe_menu = Menu()
admin_coffee = CoffeeMaker()
payment = MoneyMachine()

is_on = True

while is_on:
    print("Here is the menu:")
    options = cafe_menu.get_items()
    print(options)
    choice = input("Choose from above: ")
    if choice == "off":
        is_on == False
    elif choice == "report":
        admin_coffee.report()
        payment.report()
    else:
        drink = cafe_menu.find_drink(choice)
        if admin_coffee.is_resource_sufficient(drink):
            if payment.make_payment(drink.cost):
                admin_coffee.make_coffee(drink)

admin_coffee.is_resource_sufficient(MenuItem)

