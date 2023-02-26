import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.car_list = []
        self.car_generator()
        self.car_speed = STARTING_MOVE_DISTANCE

    def car_generator(self):
        if random.randint(0, 6) > 4:
            car = Turtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.shapesize(1, 2)
            car.penup()
            car.setheading(180)
            new_y = random.choice(range(-200, 250, 25))
            car.goto(300, new_y)
            self.car_list.append(car)

    def move(self):
        for car in self.car_list:
            car.forward(self.car_speed)

    def add_speed(self):
        self.car_speed += MOVE_INCREMENT
