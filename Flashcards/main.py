import  tkinter as tk
from tkinter import simpledialog
import tkinter.messagebox as messagebox
import csv
import random

english_word = None
french_word = None
pick = None
Lang = None


valid_languages = ["french", "japanese"]

while True:
    user_input = tk.simpledialog.askstring("Hola!", "Which language do you wish to learn?\n"
                                                   " (French / Japanese):").lower().strip()

    if user_input is None:
       messagebox.showinfo("Goodbye!, See you again!")
       exit() ## terminates the whole program
    if user_input in valid_languages:
        break
    else:
        messagebox.showinfo("Please enter either (French or Japanese)")

if user_input == "french":
    Lang = "French"
    with open("data/french_words.csv", mode="r") as file:
        data = csv.reader(file)
        data1 = [x for x in data]  ##
elif user_input == "japanese":
    Lang = "Japanese"
    with open("data/japanese1000.csv", mode="r") as file:
        data = csv.reader(file)
        data1 = [x for x in data]  ##



def word_picker():
    pick = random.choice(data1)
    return pick[0],pick[1]


def card_skip():
    global flip_timer,english_word,french_word
    window.after_cancel(flip_timer)
    french_word,english_word = word_picker()
    canvas1.itemconfig(image_id, image=img1)
    canvas1.itemconfig(word_text,text = french_word) ## Overwriting the word
    canvas1.itemconfig(title_text,text = Lang)
    flip_timer = window.after(2000, card_flip)

def card_flip():
    canvas1.itemconfig(image_id,image = img2)
    canvas1.itemconfig(word_text,text = english_word) ## Overwriting the word
    canvas1.itemconfig(title_text,text = "English")

def prev_card():
    global flip_timer
    canvas1.itemconfig(image_id, image=img1)
    canvas1.itemconfig(word_text, text=french_word)  ## Overwriting the word
    canvas1.itemconfig(title_text, text= Lang)
    flip_timer = window.after(2000, card_flip)

BACKGROUND_COLOR = "#86D1AA"

window = tk.Tk()
window.title("Flashcards")
window.config(padx = 80,pady = 70,bg = BACKGROUND_COLOR)

canvas1 = tk.Canvas(width = 802,height = 530,bg = BACKGROUND_COLOR, highlightthickness = 0)

img1 = tk.PhotoImage(file = "images/card_front.png")
img2 = tk.PhotoImage(file = "images/card_back.png")

image_id = canvas1.create_image(400,250, image = img1)
title_text = canvas1.create_text(400,120,text = "Title",font = ("Ariel",40,"italic"),fill = "black")
word_text = canvas1.create_text(400,260,text = "word",font = ("Ariel",60,"bold"),fill = "black")
canvas1.grid(row = 1, column = 1,columnspan = 3)


# canvas1.create_image(400,250,image = img2)
# canvas1.pack()

img3 = tk.PhotoImage(file = "images/wrong.png")
img4 = tk.PhotoImage(file = "images/right.png")

#buttons

button1 = tk.Button(image = img3, command = prev_card, highlightthickness = 0, bd = 0)
button1.grid(row = 2,column = 1)

button2 = tk.Button(image = img4, command = card_skip, highlightthickness = 0, bd = 0)
button2.grid(row = 2,column = 3)

flip_timer = window.after(3000,card_skip)


window.mainloop()