# leapyear
year = int(input("enter year which you would like most"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is leap year")
        else:
            print("It is NOT Leap Year")
    else:
        print("It is leap Year")
else:
    print("It is Not Leap Year")