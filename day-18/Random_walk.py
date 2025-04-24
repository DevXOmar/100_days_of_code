from turtle import Turtle,Screen
import random

timmy = Turtle()

colour = ["red","blue","green","black"]
movement = [0,90,180,270]
timmy.pensize(15)
for x in range(200):
    timmy.color(random.choice(colour))
    timmy.setheading(random.choice(movement))
    timmy.forward(30)
screen = Screen()

