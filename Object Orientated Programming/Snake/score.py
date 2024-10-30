from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        with open("data.txt",  mode = "r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.points} | High Score: {self.high_score} ", align="center", font=("Arial", 24, "normal"))


    def increase(self):
        self.points += 1
        self.update()

    def restart(self):
        if self.points > self.high_score:
            self.high_score = self.points
            with open("data.txt", mode = "w") as data:
                data.write(f"{self.points}")
        self.points = 0
        self.update()

    def gameOver(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Arial", 28, "normal"))






