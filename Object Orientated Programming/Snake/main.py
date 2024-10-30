from turtle import Screen
from player import Player
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width = 600,height = 600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

player = Player()
food = Food()
score = Score()

screen.listen()
screen.onkey(player.up,"Up")
screen.onkey(player.down,"Down")
screen.onkey(player.left,"Left")
screen.onkey(player.right,"Right")

Game = True
while Game:
    screen.update()
    time.sleep(0.1)
    player.move()

    if player.head.distance(food) < 15:
        food.refresh()
        player.extend()
        score.increase()

    if player.head.xcor() > 290 or player.head.xcor() < -290 or player.head.ycor() > 290 or player.head.ycor() < -290:
        score.restart()
        player.reset()
        #score.gameOver()

    for segment in player.snakes:
        if segment == player.head:
            pass
        elif player.head.distance(segment) < 10:
            score.restart()
            player.reset()
            #score.gameOver()

screen.exitonclick()