from turtle import Turtle,Screen
timmy = Turtle()
def Triangle():
    timmy.forward(100)
    timmy.right(120)
    timmy.forward(100)
    timmy.right(120)
    timmy.forward(100)
    timmy.home()

def square():
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.home()

def Pentagon():
    for x in range(4):
        timmy.forward(100)
        timmy.right(72)
    timmy.forward(100)
    timmy.home()
def Hexagon():
    for x in range(5):
        timmy.forward(100)
        timmy.right(60)
    timmy.forward(100)
    timmy.home()
def Heptagon():
    for x in range(6):
        timmy.forward(100)
        timmy.right(360//7)
    timmy.forward(100)
    timmy.home()
def Octagon():
    for x in range(7):
        timmy.forward(100)
        timmy.right(360//8)
    timmy.forward(100)
    timmy.home()
def Nonagon():
    for x in range(8):
        timmy.forward(100)
        timmy.right(360//9)
    timmy.forward(100)
    timmy.home()
def Decagon():
    for x in range(9):
        timmy.forward(100)
        timmy.right(360//10)
    timmy.forward(100)
    timmy.home()
Triangle()
square()
Pentagon()
Hexagon()
Heptagon()
Octagon()
Nonagon()
Decagon()
screen = Screen()
screen.exitonclick()