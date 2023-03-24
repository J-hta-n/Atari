from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 5)
        self.pu()
        self.goto(x, y)

    # def left(self):
    #     self.goto(self.xcor()-20, self.ycor())
    #
    # def right(self):
    #     self.goto(self.xcor()+20, self.ycor())