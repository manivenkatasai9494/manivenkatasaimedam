print("welcome to print calculator")
Total_bill = input("what was the bill")
percentage = input("what percent would you like to give to worker")
tip = (float(percentage) * float(Total_bill)) / 100
bill_after_tip = float(tip) + float(Total_bill)
split = input("how many persons to split the bill")
each_person = float(bill_after_tip) / float(split)
print(f"each person should pay{ each_person }")