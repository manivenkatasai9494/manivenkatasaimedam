# Rand_bill_payer
import random

names = input("Enter all Names")
split = names.split(",")
pay_bill = random.choice(split)
print(pay_bill)