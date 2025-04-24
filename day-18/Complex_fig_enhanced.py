## An enhanced and simplified version of the code after analysing the pattern/ flow of logic.
from turtle import Turtle,Screen
timmy = Turtle()
# timmy.speed(10)
for x in range(3,11):
    for y in range(x-1):
        timmy.forward(100)
        timmy.right(360//x)
    timmy.forward(100)
    timmy.home()
screen = Screen()
screen.exitonclick()