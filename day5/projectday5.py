#password generator

letter_in = int(input("How many letters would you like in your password?\n"))
symbol_in = int(input("How many symbols would you like?\n"))
number_in = int(input("How many numbers would you like?\n"))

import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '-']

password = []
for n in range(1, letter_in + 1):
    randc = random.choice(letters)
    password.append(randc)


for n in range(1, number_in +1):
    randn = random.choice(numbers)
    password.append(randn)

for n in range(1, symbol_in + 1):
    rands = random.choice(symbols)
    password.append(rands)

random.shuffle(password)

pass_word = ""
for n in password:
    pass_word = pass_word + n


print(f"Your password is : {pass_word}")




