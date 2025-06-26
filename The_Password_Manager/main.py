import tkinter as tk
from tkinter import messagebox
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
    passw = "".join(passw) ## A string.
    print(passw)
    entry3.insert(0,passw)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_info():
    website1 = entry1.get()
    user_name = entry2.get()
    password = entry3.get()

    if len(website1) ==0 or len(user_name) == 0 or len(password) == 0: ## No fields empty condition.
        messagebox.showinfo(title = "Oops",message = "Please fill the empty fields.")

    else:
        # The dialogue box.
        if messagebox.askokcancel(title = "Confirmation",message = "The details entered:\n"
                                                                   f"Email: {user_name}\n"
                                                                   f"Password: {password}\n"
                                                                   f" Do you wish to save?"):

            str1 = f"{website1} || {user_name} || {password}\n"
            with open("data.txt",mode = "a") as file:
                file.write(str1)
                entry1.delete(0, tk.END)
                entry3.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx = 40,pady = 30) ## does the job.

#canvas
canvas1 = tk.Canvas(width = 210,height = 196,)
img1 = tk.PhotoImage(file = "logo.png")
canvas1.create_image(105,98,image = img1) ## Height adjustion of the image
canvas1.grid(row = 0, column = 2)

#Entry
entry1 = tk.Entry(width = 35)
entry1.focus()
entry1.grid(row = 1,column = 2,columnspan = 2)

entry2 = tk.Entry(width = 35)
entry2.grid(row = 2, column = 2, columnspan = 2)
entry2.insert(0,"god.s.m.o.97@gmail.com")


entry3 = tk.Entry(width = 19)
entry3.grid(row = 3, column = 2,columnspan = 1,padx = 0)

#button
button1 = tk.Button(text = "Generate password",width = 12,command = generate_password)
button1.grid(row = 3,column = 3,columnspan = 1,padx = 0)
# button1.place(x = 260,y = 260)

button2 = tk.Button(text = "Add",width = 33,command = get_info)
button2.grid(row = 4,column = 2,columnspan = 2)

#label
label1 = tk.Label(text = "Website:")
label1.grid(row = 1,column =1)

label2 = tk.Label(text = "Email/Username")
label2.grid(row = 2,column =1)

label3 = tk.Label(text = "Password:")
label3.grid(row = 3,column =1)

window.mainloop()
