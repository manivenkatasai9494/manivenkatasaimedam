# Guess_Num
#Computer choces any number between 1 to 100
import random
print("Welcome To guessing Number")
print("I'm Thinking Number Between")
chosen_Type = input("which type you want to choose 'hard' or 'easy' :")
comp_choice = random.randint(1,100)
print("computer chosed the number between 1 to 100")
if chosen_Type == 'easy':
    user_choice = " "
    for i in range(0,10):
        print(f"you have {10-i} chances")
        user_choice = int(input("enter u r choice"))
        if user_choice == comp_choice:
            print(f"you chose {user_choice} and comp chosed{comp_choice}")
            break
        elif user_choice > comp_choice:
            print("You entered greater than comp chosen number")
            continue
        elif user_choice < comp_choice:
            print("You entered less than comp chosen number")
            continue
        else:
            print("Invalid")
elif chosen_Type == 'hard':
    user_choice = " "
    for i in range(0, 5):
        print(f"you have {5 - i} chances")
        user_choice = int(input("enter u r choice"))
        if user_choice == comp_choice:
            print(f"you chose {user_choice} and comp chosed{comp_choice}")
            break
        elif user_choice > comp_choice:
            print("You entered greater than comp chosen number")
            continue
        elif user_choice < comp_choice:
            print("You entered less than comp chosen number")
            continue
        else:
            print("Invalid")