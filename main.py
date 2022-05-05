from resources import resources
from MENU import MENU

machine_on = True
profit = 0

def is_resources_sufficient(order_ingredients):
    """Checks if resources are sufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


def make_coffe(drink_name, order_ingredients):
    """Deduct ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}.")

def amount_coins():
    """Returns total calculated from coins"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def transaction_ok(money_received, drink_cost):
    """Return true when payment is sufficient, false when not"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your ${change} change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, not enough. Money has been refunded")
        return False

while machine_on:
    choice = input("What would you like to drink? (espresso/latte/cappuccino): ").lower()

    if choice == 'off':
        print("Good bye!")
        machine_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Profit: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = amount_coins()
            if transaction_ok(payment, drink["cost"]):
                make_coffe(choice, drink["ingredients"])
