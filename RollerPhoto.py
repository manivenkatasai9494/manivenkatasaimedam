print("Welcome To Rollercoaster Ride")
height = int(input("Enter Your Height"))
if height > 120:
    print("You Can Enjoy Rollercoaster Ride")
    age = int(input("Enter Your age"))
    if age < 12:
        bill = 5
        print(f"You Should Pay{bill} dollars")
    elif age < 18:
        bill = 7
        print(f"You Should Pay {bill} Dollars")
    else:
        bill = 12
        print(f"You Should Pay {bill}")
else:
    print("You Are Not Not allowed To Ride")
Take_photo = int(input("Are You Want To Take Photo? Y or N"))
if Take_photo == Y:
    print("You Pay Extra $3")
    bill = bill + 3
print(f"Your Total Bill is {bill} ")
# Roller_photo