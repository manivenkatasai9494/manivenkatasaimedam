import os

ration = {"water": 1000, "milk": 1000, "coffee": 400, "cash": 0}


def coldcoffee():
    try:
        user_cash = int(input("Give cash to Coffee machine"))
    except Exception:
        print("Enter Valid Option")
    else:

        if user_cash < menu["coldcoffee"]["cost"]:
            print("Your money is not enough")
            print(f"your money {user_cash} was returned")
            return
        elif user_cash > menu["coldcoffee"]["cost"] and ration["water"] > menu["coldcoffee"]["ingredients"]["water"] and \
                ration["milk"] > menu["coldcoffee"]["ingredients"]["milk"] and ration["coffee"] > \
                menu["coldcoffee"]["ingredients"]["coffee"]:
            if user_cash > menu["coldcoffee"]["cost"]:
                change = user_cash - menu["coldcoffee"]["cost"]
                print(f"here is your change : {change}")

            ration["water"] = ration["water"] - menu["coldcoffee"]["ingredients"]["water"]
            ration["milk"] = ration["milk"] - menu["coldcoffee"]["ingredients"]["milk"]
            ration["coffee"] = ration["coffee"] - menu["coldcoffee"]["ingredients"]["coffee"]
            ration["cash"] = ration["cash"] + menu["coldcoffee"]["cost"]
            print("Here is Your coffee is Ready for You")



        else:
            print(f"Coffe Machine Ration Is not enough")
            return


def hotcoffee():

    try:
        user_cash = int(input("Give cash to Coffee machine"))
    except Exception:
        print("Enter Valid Option")
    else:

        if user_cash < menu["hotcoffee"]["cost"]:
            print("Your money is not enough")
            print(f"your money {user_cash} was returned")
            return
        elif user_cash > menu["hotcoffee"]["cost"] and ration["water"] > menu["hotcoffee"]["ingredients"]["water"] and \
                ration["milk"] > menu["hotcoffee"]["ingredients"]["milk"] and ration["coffee"] > \
                menu["hotcoffee"]["ingredients"]["coffee"]:
            if user_cash > menu["hotcoffee"]["cost"]:
                change = user_cash - menu["hotcoffee"]["cost"]
                print(f"here is your change : {change}")

            ration["water"] = ration["water"] - menu["hotcoffee"]["ingredients"]["water"]
            ration["milk"] = ration["milk"] - menu["hotcoffee"]["ingredients"]["milk"]
            ration["coffee"] = ration["coffee"] - menu["hotcoffee"]["ingredients"]["coffee"]
            ration["cash"] = ration["cash"] + menu["hotcoffee"]["cost"]
            print("Here is Your coffee is Ready for You")
        else:
            print(f"Coffe Machine Ration Is not enough")
            return


def blackcoffee():

    try:
        user_cash = int(input("Give cash to Coffee machine"))
    except Exception:
        print("Enter Valid Option")
    else:


        if user_cash < menu["blackcoffee"]["cost"]:
            print("Your money is not enough")
            print(f"your money {user_cash} was returned")
            return
        elif user_cash > menu["coldcoffee"]["cost"] and ration["water"] > menu["blackcoffee"]["ingredients"][
            "water"] and ration["milk"] > menu["blackcoffee"]["ingredients"]["milk"] and ration["coffee"] > \
                menu["blackcoffee"]["ingredients"]["coffee"]:
            if user_cash > menu["blackcoffee"]["cost"]:
                change = user_cash - menu["blackcoffee"]["cost"]
                print(f"here is your change : {change}")

            ration["water"] = ration["water"] - menu["blackcoffee"]["ingredients"]["water"]
            ration["milk"] = ration["milk"] - menu["blackcoffee"]["ingredients"]["milk"]
            ration["coffee"] = ration["coffee"] - menu["blackcoffee"]["ingredients"]["coffee"]
            ration["cash"] = ration["cash"] + menu["hotcoffee"]["cost"]
            print("Here is Your coffee is Ready for You")
        else:
            print(f"Coffe Machine Ration Is not enough")
            return


def clearscreen():
    os.system('cls')


menu = {
    "coldcoffee": {
        "ingredients": {
            "water": 50,
            "milk": 150,
            "coffee": 18,
        },
        "cost": 100,
    },
    "hotcoffee": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 150,
    },
    "blackcoffee": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 200,
    }
}


def report():
    print("------------------------------")
    print("water :", ration["water"])
    print("milk :", ration["milk"])
    print("coffee :", ration["coffee"])
    print(f"cash :", ration["cash"])
    print("------------------------------")


def coffee():
    power = input("Coffemachine 1.ON or 2.OFF :")
    if power == '1':
        print("Coffee machine Running")
    elif power == '2':
        print(f"Coffee machine was OFFed")
        return
    choice = input(
        "1.coldcoffee=$100\n2.hotcoffee=$150\n3.blackcoffee=$200\n4.report\n5.Clear Screen\n6.exit\nenter choice : ")
    if choice == '1':
        coldcoffee()
    elif choice == '2':
        hotcoffee()
    elif choice == '3':
        blackcoffee()
    elif choice == '4':
        report()
    elif choice == '6':
        print("Program End")
        return

    elif choice == '5':
        clearscreen()

    else:
        print("Invalid input")
    coffee()



coffee()
