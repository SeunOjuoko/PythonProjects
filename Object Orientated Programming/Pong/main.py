from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')

#Hides the creation animation
screen.tracer(0)

player1 = Paddle((-350,0))
player2 = Paddle((350,0))
ball = Ball((0,0))
score = Score()

screen.listen()
screen.onkey(player1.up,"w")
screen.onkey(player1.down,"s")
screen.onkey(player2.up,"Up")
screen.onkey(player2.down,"Down")

Game = True

while Game:
    time.sleep(ball.speed)
    screen.update()
    score.update()
    ball.move()


    #Detects collision with wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.wallBounce()

    #Detects collision with paddle
    if ball.distance(player1) < 50 and ball.xcor() < -320 or ball.distance(player2) < 50 and ball.xcor() > 320:
        ball.paddleBounce()


    if ball.xcor() > 380:
        ball.reset()
        score.player1Scores()

    if ball.xcor() < -380:
        ball.reset()
        score.player2Scores()









screen.exitonclick()