from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.setheading(-90)

    def move(self, x):
        self.forward(x)

    #bounce off the top wall
    def v_bounce(self):
        self.setheading(-self.heading())

    #bounce off the side walls
    def h_bounce(self):
        self.setheading(180-self.heading())

    #bounce off the paddle. bounce angle depends on which part of the paddle was hit.
    def paddle_bounce_l(self):
        self.setheading(randint(120,160))

    def paddle_bounce_c(self):
        self.setheading(randint(60,120))

    def paddle_bounce_r(self):
        self.setheading(randint(20,60))