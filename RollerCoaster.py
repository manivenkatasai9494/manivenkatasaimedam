# Rollercoaster
print("welcome to Rollercoaster ride")
height = int(input("enter u r height :"))
if height > 120:
    print("You Can Enjoy Rollercoaster")
    age = int(input("enter u age : "))
    if age < 12:
        print("Please Pay $5")
    elif age <= 18:
        print("pay $7")
    elif age > 18:
        print("please pay $12")
else:
    print("Your are Not Allowed to Ride ")