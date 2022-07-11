MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

# water = resources["water"]
# milk = resources["milk"]
# coffee = resources["coffee"]
# money = 0


condition = True
profit = 0
resources["money"] = 0

def check_if_enough(target_drink):
    for item in target_drink:
        if target_drink[item] >= resources[item]:
            print(f"​Sorry there is not enough {item}")
            return False
    return True

def check_money():
    print("Insert coins")
    num_of_quart = int(input("How many quarters?: "))
    num_of_dimes = int(input("How many dimes?: "))
    num_of_nickles = int(input("How many nickles?: "))
    num_of_pennies = int(input("How many pennies?: "))
    total = 0.25 * num_of_quart + 0.1 * num_of_dimes + num_of_nickles * 0.05 + num_of_pennies * 0.01
    return total

def successful_transaction(money_recived, cost_of_drink):
    if money_recived >= cost_of_drink:
        global profit
        profit += cost_of_drink
        resources["money"] = profit
        change = round(money_recived - cost_of_drink, 2)
        print(f"Your change is ${change}")
        return True
    else:
        print("It's not enough money")
        return False

def make_coffee(drink_name, order_ingridients):
    for item in order_ingridients:
        resources[item] -= order_ingridients[item]
    print(f"It`s your {drink_name}")

while condition:

    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    if choice == "off":
        print("See You Later")
        condition = False
    elif choice == "report":
        for item in resources:
            print(f"{item}: {resources[item]}")
    else:
        drink = MENU[choice]
        if check_if_enough(drink["ingredients"]):
            payment = check_money()
            if successful_transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
        




