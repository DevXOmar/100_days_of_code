from turtle import Turtle,Screen
from movement import Move
import random
from food import Food
import time
from snake_cont import Body

snake_head = Turtle()
snake_head.shape("square")
snake_head.color("green")
snake_head.shapesize(0.6,1)

screen = Screen()
screen.screensize(700,700)
screen.bgcolor("black")
screen.title("The Snake Game")

food = Food()

score_board = Turtle()
score_board.color("white")
score_board.penup()
score_board.hideturtle()
score_board.goto(220,280)

segments = []

score = 0

mive = Move(snake_head)


game_running = True
while game_running:

    snake_head.penup()
    snake_head.forward(2)

    screen.listen()
    screen.onkey(mive.up, "Up")
    screen.onkey(mive.down, "Down")
    screen.onkey(mive.left, "Left")
    screen.onkey(mive.right, "Right")
    # if x % 500 == 0:
    #     food.goto(random.randint(-320,320),random.randint(-330,330))
    if snake_head.distance(food) < 15:

        food.refresh()
        score += 1
        score_board.clear()
        score_board.write(f"The score is {score-1}",align = "center", font = ("Ariel",16,"normal"))

        new_segment = Turtle("square")
        new_segment.color("green")
        new_segment.shapesize(0.6,0.6)
        segments.append(new_segment)

    if snake_head.xcor() == 348 or snake_head.xcor() == -348 :
        game_running = False
        # score_board.write("GAME OVER")
        # time.sleep(1)

    elif snake_head.ycor() == 348 or snake_head.ycor() == -348 :
        game_running = False

