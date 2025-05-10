from turtle import Turtle,Screen
starting_positions = [(0,0),(-20,0),(-40,0)]
Move_distance = 2

class Body(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for x in starting_positions:
            new_segment = Turtle("square")
            new_segment.color("green")
            new_segment.penup()
            new_segment.goto(x)
            self.segments.append(new_segment)

    def crawling(self):
        for x in range(len(starting_positions)-1,0,-1):
            xcoor = self.segments[x-1].xcor()
            ycoor = self.segments[x - 1].ycor()
            self.segments[x].goto(xcoor,ycoor)
        # self.segments[0].left(90)
        self.segments[0].forward(Move_distance)




