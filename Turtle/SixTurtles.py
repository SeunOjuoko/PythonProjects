from turtle import Turtle, Screen
import turtle as t
import random

screen = Screen()
screen.setup(width = 500,height = 400)
Bet = screen.textinput(title = "BET!!!", prompt = "Enter the colour of the Turtle that will win the race?")
colours = ["red","orange","yellow","green","blue","indigo","violet"]

Tyrone = Turtle("turtle")
Tyrone.color(colours[i])
Tyrone.penup()
Tyrone.goto(-230,y = 75)

Tyler = Turtle("turtle")
Tyler.color(colours[5])
Tyler.penup()
Tyler.goto(x = -230,y = 50)

Tyson = Turtle("turtle")
Tyson.color(colours[4])
Tyson.penup()
Tyson.goto(x = -230,y = 25)

Tyreece = Turtle("turtle")
Tyreece.color(colours[3])
Tyreece.penup()
Tyreece.goto(x = -230,y = 0)

Tyrell = Turtle("turtle")
Tyrell.color(colours[2])
Tyrell.penup()
Tyrell.goto(x = -230,y = -25)

Tykwan = Turtle("turtle")
Tykwan.color(colours[1])
Tykwan.penup()
Tykwan.goto(x = -230,y = -50)

Tylene = Turtle("turtle")
Tylene.color(colours[0])
Tylene.penup()
Tylene.goto(x = -230,y = -75)