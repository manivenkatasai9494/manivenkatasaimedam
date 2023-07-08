

print("___________________________________")
print("welcome to Love Calculator")
print("___________________________________")
name1 = str(input("what is u name:"))
print("___________________________________")
name2 = str(input("what is u r crush name:"))
print("___________________________________")
string = str(name1) + str(name2)
Total_string = string.lower()
print("\n")
T = Total_string.count("t")
R = Total_string.count("r")
U = Total_string.count("u")
E = Total_string.count("e")
Total_True = T + R + U + E
print("___________________________________")
print(f"TRUE Total = {Total_True}")
print("\n")
L = Total_string.count("l")
O = Total_string.count("o")
V = Total_string.count("v")
E = Total_string.count("e")
Total_Love = L + O + V + E

#Total of Love
print("___________________________________")
print(f"Love Total is = {Total_Love}")
print("___________________________________")
print("\n")
#converting int to strings
answer = str(Total_True) + str(Total_Love)
print("___________________________________")
#printing occurs
print(f"T occurs {T} times")
print(f"R occurs {R} times")
print(f"U occurs {U} times")
print(f"E occurs {E} times")
print("___________________________________")
print("\n")
print("___________________________________")
print(f"L occurs {L} times")
print(f"O occurs {O} times")
print(f"V occurs {V} times")
print(f"E occurs {E} times")
print("___________________________________")
print("\n")

#total love score is
print("___________________________________")
print(f"Love Score is {answer}%")
print("___________________________________")
ans_int = int(answer)

if ans_int < 10 or ans_int > 90:
    print(f"Your score is {answer}, you go together like coke and mentos.")
elif ans_int >= 40 and ans_int <= 50:
    print(f"Your score is {answer}, you are alright together.")
else:
    print(f"Your score is {answer}.")