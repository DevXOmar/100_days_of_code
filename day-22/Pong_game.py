from turtle import Turtle,Screen
from figure import Figure
from movement import Move

screen = Screen()
screen.bgcolor("black")
screen.screensize(600,600)
screen.title("The Pong Game")

def mid_line():
    dash = Turtle()
    dash.hideturtle()
    dash.color("white")
    dash.penup()
    dash.goto(0,330)
    dash.setheading(270)
    dash.pendown()
    ycoor = dash.ycor()
    screen.tracer(0) #
    def dashed_line():  ## The dashed line Logic.
        dash.forward(10)
        dash.penup()
        dash.forward(10)
        dash.pendown()
        dash.forward(10)
    while ycoor > -340:
        ycoor = dash.ycor()
        dashed_line()
    screen.update() #

left_bar = Figure(-340)

right_bar = Figure(330)

mid_line()
print(left_bar.position())

## movement :
def up():
    print("up pressed")
    ycoor = left_bar.ycor()+20
    left_bar.goto(left_bar.xcor(),ycoor)

def down():
    print("down pressed")
    ycoor = left_bar.ycor()-20
    left_bar.goto(left_bar.xcor(),ycoor)

screen.listen()
screen.onkey(up,key = "w")
screen.onkey(down,key = "s")

screen.mainloop()