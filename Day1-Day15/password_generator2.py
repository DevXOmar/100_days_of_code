###################
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

passw = []
for x in range(nr_letters):
     x = random.choice(letters)
     passw.append(x)
for x in range(nr_symbols):
    x = random.choice(symbols)
    passw.append(x)
for x in range(nr_numbers):
    x = random.choice(numbers)
    passw.append(x)
#print(passw)
random.shuffle(passw) #shufling our current list.
#print(passw)
#### converting our list into a string.
passw = "".join(passw)
print(f"The total length of your password is {len(passw)}.")
print(passw)
