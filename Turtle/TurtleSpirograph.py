from turtle import Turtle, Screen
import turtle as t
import random

Tyrone = t.Turtle()
Tyrone.shape("turtle")
Tyrone.position()
(0.00,0.00)
Tyrone.speed("fastest")
t.colormode(255)

def random_colour():
    r = random.randint(0, 225)
    g = random.randint(0, 225)
    b = random.randint(0, 225)
    colour = (r, g, b)
    return colour

def draw(size):
    for i in range(int(360/size)):
        Tyrone.color(random_colour())
        Tyrone.circle(100)
        Tyrone.setheading(Tyrone.heading() + size)

draw(5)

screen = Screen()
screen.exitonclick()