# pizza

print("welcome To Python Pizza")
#which size You want to take pizza
size = input("Which Type of Pizza You Need ? 'S for small' or 'M for Medium' or 'L for Large' :-")
if  size == "S":
  cost = 15
  print(f"You Should Pay ${cost} ")
elif size == "M":
  cost = 20
  print(f"You Should Pay ${cost} ")
else:
  cost = 25
  print(f"You Should Pay ${cost} ")
#cost of pizza is equal to  pizza_cost = cost
pizza_cost = cost
#input for pepper Y or N
pepp = input("If You need pepperoni for Small = S,Medium or Large = N :-")

if size == "S" :
  cost_of_pepp = 3
else :
  cost_of_pepp = 3
#cost of pepper
pepper = cost_of_pepp
cheese = input("U need cheese ? Y or N")
#you need cheese or not
print("cost of cheese  is + 1  Y or N ")
if cheese ==  "Y" :
   cost_of_cheese = 1
else :
   cost_of_cheese = 0
  #total bill is

Total_bill = int(cost_of_pepp) + int(cost_of_cheese) + int(pizza_cost)
print(f"Total Bill You should pay ${Total_bill}")
