class Move:
    def __init__(self,snake):
        self.mike = snake
        self.direction = "Right"
    def up(self):
        if self.direction != "Down":  ## If it is moving down, it can't go up.
           self.mike.setheading(90)
           self.direction = "Up"
    def down(self):
        if self.direction != "Up":
           self.mike.setheading(270)
           self.direction = "Down"
    def left(self):
        if self.direction != "Right":
           self.mike.setheading(180)
           self.direction = "Left"
    def right(self):
        if self.direction != "Left":
            self.mike.setheading(0)
            self.direction = "Right"

