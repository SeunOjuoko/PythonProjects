from turtle import Turtle, Screen

Tyrone = Turtle()
Tyrone.shape("turtle")
Tyrone.color("blue")

for i in range(4):
    Tyrone.forward(100)
    Tyrone.right(90)

screen = Screen()
screen.exitonclick()