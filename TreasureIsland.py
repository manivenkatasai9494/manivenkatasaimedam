print("Welcome To Treasure Island,You mission is to find the Treasure")
choice1 = input(
    "You are crossroad where you want to go ? 'left' or 'right'".lower())
if choice1 == "left":
    choice2 = input("You are at gate you want 'swim' or 'wait'".lower())
    if choice2 == "wait":
        choice3 = input(
            "which door you want to go 'blue' or 'red' or 'yellow'".lower())
        if choice3 == "yellow":
            print("You won The Game")
        else:
            print("game over")
    else:
        print("game over!!!")

else:
    print("game over!!!")