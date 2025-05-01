from turtle import Turtle,Screen
timmy = Turtle()
tura = Turtle()
screen = Screen()

def move_forward():
    timmy.forward(10)

def move_back():
    timmy.right(180)
    timmy.forward(10)

def move_left():
    timmy.left(90)
    timmy.forward(10)

def move_right():
    timmy.right(90)
    timmy.forward(10)
def clean():
    screen.clear()

def movi():
    timmy.home()
screen.listen()
screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_back)
screen.onkey(key = "a", fun = move_left)
screen.onkey(key = "d", fun = move_right)
screen.onkey(key = "c", fun = clean)
screen.onkey(key = "g", fun = movi)
screen.exitonclick()