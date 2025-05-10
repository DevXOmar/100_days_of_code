from turtle import Turtle,Screen
import random
import time

class Food(Turtle): # It is now a child-class.
   def __init__(self):
       super().__init__()
       self.shape("circle")
       self.shapesize(0.5,0.5)
       self.color("red")


   def refresh(self):

       xcoor = random.randint(-320,320)
       ycoor = random.randint(-320,320)
       self.penup()
       self.goto(xcoor,ycoor)





