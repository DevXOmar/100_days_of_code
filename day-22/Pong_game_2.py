from turtle import Turtle,Screen
import random

screen = Screen()
screen.bgcolor("black")
screen.screensize(600,600)
screen.title("The Pong Game")
screen.tracer(0)

score1 = 0
score2 = 0

score_board1 = Turtle()
score_board1.color("white")
score_board1.hideturtle()
score_board1.penup()
score_board1.goto(-140,280)
score_board1.write(f"SCORE : {score1}", align = "center", font=("Baskerville", 32, "normal"))


score_board2 = Turtle()
score_board2.color("white")
score_board2.hideturtle()
score_board2.penup()
score_board2.goto(140,280)
score_board2.write(f"SCORE : {score2}", align = "center", font=("Baskerville", 32, "normal"))

left_bar = Turtle()
left_bar.color("white")
left_bar.shape("square")
left_bar.shapesize(4, 0.8)
left_bar.penup()
left_bar.goto(-340,0)

right_bar = Turtle()
right_bar.color("white")
right_bar.shape("square")
right_bar.shapesize(4, 0.8)
right_bar.penup()
right_bar.goto(330,0)

ball = Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
current_dir = random.randint(0,360)
ball.setheading(current_dir)
# print("initial direction: ",current_dir)

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
def up():
    # print("up pressed")
    if left_bar.ycor() < 300:
        ycoor = left_bar.ycor()+40
        left_bar.goto(left_bar.xcor(),ycoor)

def down():
    # print("down pressed")
    if left_bar.ycor() >-280 :
        ycoor = left_bar.ycor()-40
        left_bar.goto(left_bar.xcor(),ycoor)
def upr():
    # print("up pressed")
    if right_bar.ycor() <300 :
        ycoor = right_bar.ycor()+40
        right_bar.goto(right_bar.xcor(),ycoor)

def downr():
    # print("down pressed")
    if right_bar.ycor() > -280 :
        ycoor = right_bar.ycor()-40
        right_bar.goto(right_bar.xcor(),ycoor)
def move_ball():
    global score1,score2
    ball.forward(6)

    # Top and Bottom walls
    if ball.ycor()>340 or ball.ycor() <-340 :
        current_dir = ball.heading()
        ball.setheading(360-current_dir)

    # Paddle collision
    if ball.xcor()>320 and right_bar.ycor()-60 < ball.ycor()<right_bar.ycor()+60 or\
        ball.xcor()<-320 and left_bar.ycor()-60 <ball.ycor()<left_bar.ycor()+60:
        current_dir = ball.heading()
        ball.setheading(180-current_dir)

    if ball.xcor() >350:
        score1 += 1
        ball.goto(0,0)
        ball.setheading(180 - ball.heading())
    elif ball.xcor() <-350:
        score2 += 1
        ball.goto(0,0)
        ball.setheading(180-ball.heading())

mid_line()
screen.update() ## After tracer it directly showed this.
while True:
    screen.update() ## we need to keep them updating
    screen.listen()
    screen.onkey(up,key = "w")
    screen.onkey(down,key = "s")
    screen.onkey(upr,key="Up")
    screen.onkey(downr,key = "Down")
    score_board1.clear()
    score_board1.write(f"SCORE : {score1}", align="center", font=("Baskerville", 32, "normal"))
    score_board2.clear()
    score_board2.write(f"SCORE : {score2}", align="center", font=("Baskerville", 32, "normal"))
    if score1 == 10:
        score_board1.clear()
        score_board1.goto(-140,260)
        score_board1.write(f"SCORE : {score1}\n You WIN !", align="center", font=("Baskerville", 32, "normal"))
        break
    elif score2 == 10:
        score_board2.clear()
        score_board2.goto(140, 250)
        score_board2.write(f"SCORE : {score2}\n You WIN !", align="center", font=("Baskerville", 32, "normal"))
        break
    move_ball()
screen.mainloop()
