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
screen.setup(width=700, height=700)  # Sets the actual window size
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)  # Batch screen updates

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

segments = []

# Define movement functions
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
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# Main game loop
game_running = True

while game_running:
    screen.update()
    screen.listen()
    screen.onkey(up, "Up")
    screen.onkey(down, "Down")
    screen.onkey(left, "Left")
    screen.onkey(right, "Right")

    head_x, head_y = head.xcor(), head.ycor()

    # Food Collision
    if head.distance(food) < 16:
        xcoor = random.randint(-200, 200)
        ycoor = random.randint(-200, 200)
        food.goto(xcoor, ycoor)
        score += 1

        # Add a new segment
        new_segment = Turtle("square")
        new_segment.color("red")
        new_segment.penup()
        segments.append(new_segment)

    # Wall Collision
    if head.xcor() > screen.window_width() // 2 - 20 or head.xcor() < -screen.window_width() // 2 + 20 or \
       head.ycor() > screen.window_height() // 2 - 20 or head.ycor() < -screen.window_height() // 2 + 20:
        game_running = False

    # Move the snake's body
    for i in range(len(segments) - 1, -1, -1):
        if i == 0:
            segments[0].goto(head_x, head_y)
        else:
            segments[i].goto(segments[i - 1].xcor(), segments[i - 1].ycor())

        # Self-Collision
        if i > 0 and head.distance(segments[i]) < 5:
            game_running = False

    # Move the head
    move()

    # Update the score
    score_board.clear()
    score_board.write(f"SCORE : {score}", align="center", font=("Arial", 16, "normal"))

    time.sleep(0.1)

screen.mainloop()