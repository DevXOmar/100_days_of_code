import random
import secrets
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

low_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cap_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_low_letters = random.randint(4,6)
nr_cap_letters = random.randint(4,6)
nr_symbols = random.randint(1,3)
nr_numbers = random.randint(1,3)

def generate_password():
    passw = []
    for x in range(nr_low_letters):
        letter = secrets.choice(low_letters)
        passw.append(letter)
    for x in range(nr_cap_letters):
        letter = secrets.choice(cap_letters)
        passw.append(letter)
    for x in range(nr_symbols):
        letter = secrets.choice(symbols)
        passw.append(letter)
    for x in range(nr_numbers):
        letter = secrets.choice(numbers)
        passw.append(letter)
    random.shuffle(passw)
    passw = "".join(passw)
    print("Your secure password is: ")
    print(passw)
    
generate_password()
