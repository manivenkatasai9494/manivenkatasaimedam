# bill_payer
import random
#am entered dynamically all my friends names
all_names = input('Enter all of your names:')
#by using split(",")  function am splitiing their names ['name','name','name']
split_names = all_names.split(",")
#by using len()function am checking how many names are present
#in x am storing length
x = len(split_names)
#by using randint pc going pick one number from (0,x-1)  (-1)becoz leghth is normal way number but random is starts from 0 to x-1
rand_num = random.randint(0, x - 1)
#storing number to rand_num
pay_name = split_names[rand_num]
print(f"{pay_name} is going to pay bill")