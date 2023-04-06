import random
num_letters = int(input("How many letters would you like in the password?: "))
num_numbers = int(input("How many numbers would you like in the password?: "))
num_symbols = int(input("How many symbols would you like in the password?: "))

list_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list_number = [1,2,3,4,5,6,7,8,9]
list_symbol = ['!','@','#','$','%','&','*','(',')','-','+']

final_pass = []

#letters
for letter in range(0,num_letters):
    is_lower = random.randint(0,1)
    if is_lower == 0:
        rand_letter = random.randint(0,len(list_letter) - 1)
        final_pass.append(list_letter[rand_letter].lower())
    else:
        rand_letter = random.randint(0,len(list_letter) - 1)
        final_pass.append(list_letter[rand_letter])
#nums
for num in range(0,num_numbers):
    rand_number = random.randint(0,len(list_number) - 1)
    final_pass.append(str(list_number[rand_number]))
#symbols
for symb in range(0,num_symbols):
    rand_symbol = random.randint(0,len(list_symbol) - 1)
    final_pass.append(list_symbol[rand_symbol])

random.shuffle(final_pass)


print("".join(final_pass))
