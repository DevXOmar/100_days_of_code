from turtle import Turtle,Screen
### Super cool.
timmy = Turtle()
timmy.shape("turtle")
def square():
    dashed()
    timmy.right(90)
    dashed()
    timmy.right(90)
    dashed()
    timmy.right(90)
    dashed()
# for x in range(10):
def dashed():
    for x in range(3):
        timmy.forward(10)
        timmy.up()
        timmy.forward(10)
        timmy.down()
        timmy.forward(10)

square()
timmy.home()
screen = Screen()
screen.exitonclick()