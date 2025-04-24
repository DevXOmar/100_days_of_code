from turtle import Turtle,Screen
import random
timmy = Turtle()
screen = Screen()
screen.colormode(255)
timmy.speed(0)
for x in range(0,361,5):
    tuple1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    timmy.pencolor(tuple1)
    timmy.setheading(x)
    timmy.circle(100)
screen.exitonclick() # else the screen window closes as soon as animation is done.
