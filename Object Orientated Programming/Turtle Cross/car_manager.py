from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.start_move_distance = STARTING_MOVE_DISTANCE
        self.move_increment = MOVE_INCREMENT
        self.chance = 6


    def create(self):
        random_chance = random.randint(1, self.chance)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.move_increment)

    def increase_speed(self):
        self.move_increment += 10
        #self.chance -= 2




