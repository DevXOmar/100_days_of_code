from turtle import Turtle ,Screen
from car_mania import Car_mania
import time

screen = Screen()
screen.screensize(600,600)
screen.tracer(0)
screen.title("The Turtle Crossing Game")

timmy = Turtle()
timmy.shape("turtle")
timmy.penup()
timmy.goto(0,-300)
timmy.setheading(90)

Level = 1

score_board = Turtle()
score_board.color("black")
score_board.penup()
score_board.goto(250,270)
score_board.hideturtle()
score_board.write(f"Level : {Level}",align = "center",font = ("Baskerville", 32, "normal"))

def up():
    timmy.forward(10)

screen.listen()
screen.onkey(up,key = "w")
cars = Car_mania()

sleeping = 0.1
game_running = True
while game_running:
    time.sleep(sleeping)
    screen.update()

    cars.car_create()
    cars.move()
    for item in cars.car:
        # print(item)
        if timmy.distance(item) < 20:
            game_running = False

            score_board1 = Turtle()
            score_board1.color("black")
            score_board1.penup()
            score_board1.goto(0, 0)
            score_board1.hideturtle()
            score_board1.write("Game Over !", align="center", font=("Baskerville", 32, "normal"))
    if timmy.ycor()>310 :
        timmy.goto(0,-300)
        sleeping -= 0.04
        Level += 1
        score_board.clear()
        score_board.write(f"Level : {Level}",align = "center",font = ("Baskerville", 32, "normal"))
        if sleeping < 0:
            sleeping = 0.01
screen.exitonclick()