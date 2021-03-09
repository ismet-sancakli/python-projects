from data import MENU, resources


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients is insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}. ")
            return False
    return True


def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted or False money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global total_gain
        total_gain += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins ")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


total_gain = 0
print("Isn't it the perfect day to drink coffee? ☕☕☕")


def coffee_machine():
    is_continue = True
    coffee_list = ["espresso", "latte", "cappuccino", "off", "report"]
    while is_continue:

        choice = input("What would you like? (espresso/latte/cappuccino) :  ").lower()
        if choice == "off":
            is_continue = False
        elif choice not in coffee_list:
            print("Invalid choice. Repeat again!!!")
            coffee_machine()
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${total_gain}")
        else:
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])


coffee_machine()