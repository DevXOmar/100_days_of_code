from turtle import Turtle,Screen
class More(Turtle):
    def __init__(self,name,x,y):
        super().__init__()
        self.state_name = name
        self.xvalue = x
        self.yvalue = y
        self.tim = Turtle()
        self.tim.penup()
        self.tim.hideturtle()
        self.tim.goto(self.xvalue,self.yvalue)
        self.tim.write(self.state_name,font=("Ariel", 14, "normal"))

