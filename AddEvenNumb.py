# Add_even_num
#to print range of numbers
total = 0
start_value = int(input("Enter starting value : "))
End_value = int(input("enter end value : ")) + 1

for number in range(start_value, End_value, 2):
    if number % 2 != 0:
        total = total + number
print(total)