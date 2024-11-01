from turtle import Turtle
from car_manager import *

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)

    def moveUp(self):
        self.forward(MOVE_DISTANCE)

    def nextLevel(self):
        self.goto(STARTING_POSITION)




