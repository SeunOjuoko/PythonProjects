from turtle import Turtle, Screen
import random

Tyrone = Turtle()
Tyrone.shape("turtle")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

sides = 3

def Caluclate(sides):
    angle = 360 / sides
    return angle

for i in range(7):
    angle = Caluclate(sides)
    Tyrone.color(random.choice(colours))
    for i in range(sides):
        Tyrone.right(angle)
        Tyrone.forward(100)
    sides += 1

screen = Screen()
screen.exitonclick()