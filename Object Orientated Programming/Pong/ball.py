from turtle import Turtle


class Ball(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(position)
        self.x_move = 10
        self.y_move = 10
        self.speed = 0.1

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def wallBounce(self):
        self.y_move = -self.y_move

    def paddleBounce(self):
        self.x_move = -self.x_move
        self.speed *= 0.5

    def reset(self):
        self.goto(0, 0)
        self.speed = 0.1
        self.paddleBounce()


