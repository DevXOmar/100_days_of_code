from turtle import Turtle,Screen
import random
timmy = Turtle()
screen = Screen()
screen.colormode(255) ## setting this mode, saves us from bad color sequence error.
movement = [0,90,180,270]
for x in range(200):
    tuple1 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    timmy.pencolor(tuple1)
    timmy.setheading(random.choice(movement))
    timmy.forward(30)

