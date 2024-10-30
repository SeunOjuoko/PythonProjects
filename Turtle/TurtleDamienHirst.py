from turtle import Turtle, Screen
import turtle as t
import random

Tyrone = t.Turtle()
Tyrone.shape("turtle")
Tyrone.penup()
t.colormode(255)
Tyrone.speed("fastest")

colours = [(238, 237, 233), (237, 234, 238), (233, 235, 240), (215, 166, 17), (230, 239, 234), (205, 153, 99), (225, 205, 103), (161, 55, 101), (113, 187, 213), (154, 31, 58), (8, 109, 166), (42, 13, 24), (160, 29, 25), (12, 23, 52), (34, 122, 62), (59, 23, 18), (9, 32, 26), (186, 156, 173), (63, 166, 88), (171, 57, 42), (156, 208, 215), (94, 183, 167), (205, 99, 95), (240, 200, 3), (213, 174, 198), (28, 37, 105), (187, 99, 110), (163, 209, 197), (220, 177, 173), (14, 105, 56)]

y = -250
Tyrone.setpos(-250, y)

def random_colour():
    colour = random.choice(colours)
    return colour

#Hide Before
Tyrone.hideturtle()
for i in range(10):
    for j in range(10):
        colour = random_colour()
        Tyrone.dot(20, random_colour())
        Tyrone.forward(50)
    y += 50
    Tyrone.setpos(-250,y)
#Hide After
#Tyrone.hideturtle()

screen = Screen()
screen.exitonclick()