from turtle import Turtle,Screen
import random
screen = Screen()
screen.setup(500,400)
timmy = Turtle()
timmy.name = "Timmy"
mikasa = Turtle()
mikasa.name = "Mikasa"
eren = Turtle()
eren.name = "Eren"
levi = Turtle()
levi.name = "Levi"
kona = Turtle()
kona.name = "Kona"

list1 = [timmy,mikasa,eren,levi,kona]
list2 = ["blue","red","green","black","violet"]

for i,turtle in enumerate(list1):
    turtle.shape("turtle")
    turtle.color(list2[i])
    turtle.penup()
    turtle.goto(-240,(i-1)*40)

bet = screen.textinput("Start","Enter your bet: ")
print(bet)
if bet:
    run = True
while run:
    for turtle in list1:
        turtle.forward(random.randint(1,10))
        if turtle.xcor() > 232:
            winning_colour = turtle.pencolor()
            name = turtle.name
            if winning_colour == bet:
                print(f"Your chosen turtle {name} won!")
            else:
                print(f"You lost! turtle {name} won!")
            run = False


screen.exitonclick()