from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.player1_score = 0
        self.player2_score = 0

    def update(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.player1_score, align='center', font=('Arial', 80, 'normal'))
        self.goto(100, 180)
        self.write(self.player2_score, align='center', font=('Arial', 80, 'normal'))

    def player1Scores(self):
        self.player1_score += 1
        self.update()

    def player2Scores(self):
        self.player2_score += 1
        self.update()

