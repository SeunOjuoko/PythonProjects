from operator import truediv
from turtle import Turtle, Screen
import random

Tyrone = Turtle()
#Tyrone.shape("turtle")
Tyrone.hideturtle()
Tyrone.pensize(10)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
angle = [0, 90, 180, 270]

move = True

while move:
    Tyrone.color(random.choice(colours))
    Tyrone.right(random.choice(angle))
    Tyrone.forward(30)

screen = Screen()
screen.exitonclick()