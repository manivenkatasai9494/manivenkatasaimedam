# Rock_paper_scissor
import random

rock = str('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

paper = str('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')


scissors = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

user_choice = input("Enter which 0 for rock, 1 for paper, 2 for scissor :")
comp_choice = random.randint(0, 2)
if user_choice == str(0) and comp_choice == 0:
    print("You choice : Rock\n")
    print(rock)
    print("computer Choice : Rock \n")
    print(rock)
    print("Your Choice and Computer Choice are same Play Again")
elif user_choice == str(0) and comp_choice == 1:
    print("You choice : Rock \n")
    print(rock)
    print("computer Choice : Paper\n")
    print(paper)
    print("Computer Won")
elif user_choice == str(0) and comp_choice == 2:
    print("You choice : Rock\n")
    print(rock)
    print("computer Choice : Scissors \n")
    print(scissors)
    print("You Won")
elif user_choice == str(1) and comp_choice == 0:
    print("You choice : Paper\n")
    print(paper)
    print("computer Choice : Rock \n")
    print(rock)
    print("You Won")
elif user_choice == str(1) and comp_choice == 1:
    print("You choice : Paper \n")
    print(paper)
    print("computer Choice : Paper \n")
    print(paper)
    print("Play Again")
elif user_choice == str(1) and comp_choice == 2:
    print("You choice : Paper \n")
    print(paper)
    print("computer Choice : Scissors\n")
    print(scissors)
    print("Computer Won")
elif user_choice == str(2) and comp_choice == 0:
    print("You choice : Scissors \n")
    print(scissors)
    print("computer Choice : Rock\n")
    print(rock)
    print("Computer Won")
elif user_choice == str(2) and comp_choice == 1:
    print("You choice : Scissors \n")
    print(scissors)
    print("computer Choice : Paper\n")
    print(paper)
    print("You Won")
elif user_choice == str(2) and comp_choice == 2:
    print("You choice : Scissors \n")
    print(scissors)
    print("computer Choice : Scissors\n")
    print(scissors)
    print("Play Again")