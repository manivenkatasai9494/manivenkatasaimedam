weight = float(input("enter your weight"))
height = float(input("enter your height"))
bmi = weight / height**2
print(bmi)
if bmi < 18.5:
    print(f"You bmi is {bmi},you are under weight")
elif bmi < 25.5:
    print(f"You bmi is {bmi},you are in normal weight")
elif bmi < 30:
    print(f"You bmi is {bmi},you are over weight")
elif bmi < 35:
    print(f"You bmi is {bmi},you are obese")
else:
    print(f"You bmi is {bmi},you are clinically obese")