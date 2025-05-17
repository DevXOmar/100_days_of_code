from turtle import Turtle
import random
COLORS = ["red","orange","yellow","green","blue","purple"]
STARTING_DIS = 5
MOVE_INCREMENT = 10

class Car_mania:
    def __init__(self):
        self.car = []
    def car_create(self):
        # for x in range(0,20):
        random_chance = random.randint(0,6)
        if random_chance == 1:
                new_car = Turtle("square")
                new_car.shapesize(1,2)
                new_car.penup()
                new_car.color(random.choice(COLORS))
                random_y = random.randint(-220,260)
                new_car.goto(320,random_y)
                self.car.append(new_car)
    def move(self):
        for item in self.car:
            item.backward(MOVE_INCREMENT)