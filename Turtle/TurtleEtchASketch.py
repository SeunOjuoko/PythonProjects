from turtle import Turtle, Screen
import random

Tyrone = Turtle()
screen = Screen()
Tyrone.shape("turtle")

def move_forwards():
    Tyrone.forward(10)

def move_backwards():
    Tyrone.backward(10)

def move_counterclockwise():
    Tyrone.left(10)

def move_clockwise():
    Tyrone.right(10)

def clear():
    Tyrone.clear()
    Tyrone.penup()
    Tyrone.home()
    Tyrone.pendown()

screen.listen()
#screen.onkey(key="space", fun = move_forwards)
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_counterclockwise, "a")
screen.onkey(move_clockwise, "d")
screen.onkey(clear, "c")
screen.exitonclick()