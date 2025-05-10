from turtle import Turtle, Screen
import random
import time

head = Turtle()
head.shape("square")
head.color("red")
head.direction = "stop"
head.penup()
head.speed(2)

screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

food = Turtle()
food.shape("circle")
food.color("green")
food.penup()

score = 0
score_board = Turtle()
score_board.goto(0, 290)
score_board.hideturtle()
score_board.penup()
score_board.color("white")

def up():
    if head.direction != "down":
        head.direction = "up"
def down():
    if head.direction != "up":
        head.direction = "down"
def left():
    if head.direction != "right":
        head.direction = "left"
def right():
    if head.direction != "left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

segments = []
game_running = True

def game_loop():
    global game_running, score
    if not game_running:
        return

    screen.update()

    screen.listen()
    screen.onkey(up, "Up")
    screen.onkey(down, "Down")
    screen.onkey(left, "Left")
    screen.onkey(right, "Right")

    # Store head's current position before moving
    head_x, head_y = head.xcor(), head.ycor()
    move()

    # Food Collision
    if head.distance(food) < 16:
        xcoor = random.randint(-200, 200)
        ycoor = random.randint(-200, 200)
        food.goto(xcoor, ycoor)
        score += 1
        score_board.clear()

        new_segment = Turtle("square")
        new_segment.color("red")
        new_segment.penup()
        new_segment.speed(0)
        segments.append(new_segment)

    # Wall Collision
    if head.xcor() > 320 or head.xcor() < -320 or head.ycor() > 320 or head.ycor() < -320:
        game_running = False
        head.direction = "stop"

    # Move segments efficiently
    for i in range(len(segments) - 1, -1, -1):
        if i == 0:
            segments[0].goto(head_x, head_y)
        else:
            segments[i].goto(segments[i-1].xcor(), segments[i-1].ycor())
        # Self-Collision
        if i > 0 and head.distance(segments[i]) < 5:
            game_running = False

    score_board.write(f"SCORE : {score}", align="center", font=("Arial", 16, "normal"))
    screen.ontimer(game_loop, 100)

# Start the game loop
game_loop()
screen.mainloop()