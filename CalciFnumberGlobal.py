import os
# calci_fnum_global

#in this calculator program i did for two numbers and in running time it asks as seconds number else we can run with starting onwards
import sys,subprocess
def calci():
    #clreating addition,subtraction.multiplication.division
    def add(fnum, snum):
        return fnum + snum

    def sub(fnum,snum):
        return fnum - snum

    def mult(fnum, snum):
        return fnum * snum

    def divi(fnum, snum):
        return fnum / snum

    global fnum
    def access():
        snum = int(input("enter second number"))

        operation = input("Which opration u need \n+\n-\n*\n/\n")

        if operation == "+":
            answer = add(fnum, snum)
            print(answer)
        elif operation == "-":
            answer = sub(fnum, snum)
            print(answer)
        elif operation == "*":
            answer = mult(fnum, snum)
            print(answer)
        elif operation == "/":
            answer = divi(fnum, snum)
            print(answer)
        else :
            print("Invalid")
        yes = input(f"if want to contin with fnum |{fnum}| 'y' ")
        if yes == 'y':
            access()
        else :
            print("program cleared\n")
            os.system("cls")
            calci()

    #creating new values
    fnum = int(input("enter First number"))
    snum = int(input("enter second number"))

    operation = input("Which opration u need \n+\n-\n*\n/\n")
    #running of program
    if operation == "+":
        answer = add(fnum, snum)
        print(answer)
    elif operation == "-":
        answer = sub(fnum, snum)
        print(answer)
    elif operation == "*":
        answer = mult(fnum, snum)
        print(answer)
    elif operation == "/":
        answer = divi(fnum, snum)
        print(answer)
    else :
        print("Invalid")
        return 0

    #asking user to continue with fnum as global and ask as 2nd number
    yes = input(f"if want to contin with fnum |{fnum}| 'y' ")
    if yes == 'y':
        access()
    elif yes == 'n':
        #run the whole program
        print("program cleared\n")
        os.system("cls")
        calci()

    else :
        print("program done")
        return 0
calci()