from turtle import Turtle, Screen

Tyrone = Turtle()
#Tyrone.shape("turtle")
Tyrone.color("coral1")

for i in range(10):
    Tyrone.forward(10)
    Tyrone.penup()
    Tyrone.forward(10)
    Tyrone.pendown()

screen = Screen()
screen.exitonclick()