from turtle import Turtle, Screen
import turtle as t
import random

Race = False
screen = Screen()
screen.setup(width = 500,height = 400)
Bet = screen.textinput(title = "BET!!!", prompt = "Enter the colour of the Turtle that will win the race?")
colours = ["red","orange","yellow","green","blue","indigo","violet"]
y_positions = [75,50,25,0,-25,-50,-75]
Turtles = []

for i in range(0,7):
    Tyrone = Turtle("turtle")
    Tyrone.color(colours[i])
    Tyrone.penup()
    Tyrone.goto(-230,y_positions[i])
    Turtles.append(Tyrone)

if Bet:
    Race = True

while Race:
    for turtle in Turtles:
        if turtle.xcor() > 230:
            Race = False
            winner = turtle.pencolor()
            if winner == Bet:
                print(f"Congratulations!!! The {winner} turtle is the winner, you won!")
            else:
                print(f"Hahaha!!! The {winner} turtle won, but you lose!")

        RandomDistance = random.randint(0,10)
        turtle.forward(RandomDistance)

screen.exitonclick()