Menu = {
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

reasources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 150,
}

def coin():
    print("Please insert coins")
    five = float(input("How many 5p? "))
    ten = float(input("How many 10p? "))
    twenty = float(input("How many 20p? "))
    fifty = float(input("How many 50p? "))
    one = float(input("How many £1? "))
    total = (five * 0.05) + (ten * 0.1) + (twenty * 0.2) + (fifty * 0.5) + (one * 1.0)
    print(f"You have entered £{total} in coins")
    return total

total = 0
machine = True
while machine == True:
    # Online Python - IDE, Editor, Compiler, Interpreter
    coffee = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee == "report":
        print(f"Water: {reasources["Water"]}ml")
        print(f"Milk: {reasources["Milk"]}ml")
        print(f"Coffee: {reasources["Coffee"]}g")
        print(f"Money: £{reasources["Money"]}")
    elif coffee == "espresso":
        if reasources["Water"] < 50:
            print(f"Not enough Water, 50ml is needed and only {reasources["Water"]}ml is left")
        elif reasources["Coffee"] < 18:
            print(f"Not enough Coffee, 18g is needed and only {reasources["Coffee"]}g is left")
        else:
            print(f"An Espresso costs £{Menu["espresso"]["cost"]}...")
            pay = coin()
            if Menu["espresso"]["cost"] <= pay:
                pay -= Menu["espresso"]["cost"]
                reasources["Water"] -= 50
                reasources["Coffee"] -= 18
                change = round(pay, 2)
                print(f"Here is your charge £{change}")
                print("Enjoy the Espresso")
            else:
                print("Not enough change")
    elif coffee == "latte":
        if reasources["Water"] < 200:
            print(f"Not enough Water, 200ml is needed and only {reasources["Water"]}ml is left")
        elif reasources["Milk"] < 150:
            print(f"Not enough Milk, 150ml is needed and only {reasources["Milk"]}ml is left")
        elif reasources["Coffee"] < 24:
            print(f"Not enough Coffee, 24g is needed and only {reasources["Coffee"]}g is left")
        else:
            print(f"A Latte costs £{Menu["latte"]["cost"]}...")
            pay = coin()
            if Menu["latte"]["cost"] <= pay:
                pay -= Menu["latte"]["cost"]
                reasources["Water"] -= 200
                reasources["Milk"] -= 150
                reasources["Coffee"] -= 24
                change = round(pay, 2)
                print(f"Here is your charge £{change}")
                print("Enjoy the Latte")
            else:
                print("Not enough change")
    elif coffee == "cappuccino":
        if reasources["Water"] < 250:
            print(f"Not enough Water, 250ml is needed and only {reasources["Water"]}ml is left")
        elif reasources["Milk"] < 100:
            print(f"Not enough Milk, 24ml is needed and only {reasources["Milk"]}ml is left")
        elif reasources["Coffee"] < 24:
            print(f"Not enough Coffee, 100g is needed and only {reasources["Coffee"]}g is left")
        else:
            print(f"A Cappuccino costs £{Menu["cappuccino"]["cost"]}...")
            pay = coin()
            if Menu["cappuccino"]["cost"] <= pay:
                pay -= Menu["cappuccino"]["cost"]
                reasources["Water"] -= 250
                reasources["Milk"] -= 100
                reasources["Coffee"] -= 24
                change = round(pay, 2)
                print(f"Here is your charge £{change}")
                print("Enjoy the Cappuccino")
            else:
                print("Not enough change")
    elif coffee == "refill":
        reasources["Water"] = 300
        reasources["Milk"] = 200
        reasources["Coffee"] = 150
        print("The Water, Milk and Coffee are refilled in the machine")
    elif coffee == "off":
        machine = False
    else:
        print("Select an available coffee")
