from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.score = 0
        self.update()

    def update(self):
        self.goto(270, 230)
        self.write(f"Score: {self.score}", align="center", font=("courier", 23, "normal"))

    def add_point(self):
        self.score += 15
        self.clear()
        self.update()
