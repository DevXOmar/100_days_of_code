import colorgram
import random
##Color.rgb - The color represented as a namedtuple of RGB from 0 to 255, e.g. (r=255, g=151, b=210)
# colors_list =[]
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tuple1 = (r,g,b)
#     colors_list.append(tuple1)
# print(colors_list)
from turtle import Turtle,Screen
timmy = Turtle()
timmy.shape("circle")
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
screen = Screen()
screen.colormode(255)## crucial line

timmy.hideturtle()
timmy.setheading(180)
timmy.penup()
timmy.forward(150)
timmy.setheading(0)

for x in range(1,100):
    timmy.dot(20,random.choice(color_list))
    timmy.penup()
    timmy.forward(30)
    timmy.pendown()
    if x % 10 == 0:
        timmy.penup()
        timmy.setheading(90)

        timmy.forward(30)
        timmy.setheading(180)

        timmy.forward(300)
        timmy.setheading(0)
screen.exitonclick()