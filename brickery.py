from turtle import Turtle
from random import choice

class Brickery():
    def __init__(self):
        self.brick_list = [] #list of all brick objects
        self.brick_cords = [] #coordinates of bricks to check for ball collision
        self.colors = ["cyan", "yellow", "tomato", "spring green", "magenta", "green yellow", "gold", 'dark orchid',
                       "indigo", "deep pink", "orange red"] #https://trinket.io/docs/colors

    #factory method to instantiate bricks at the given (x,y) position
    def make_brick(self,x,y):
        brick = Turtle()
        brick.shape("square")
        brick.shapesize(1,4)
        brick.pu()
        brick.goto(x,y)
        brick.color(choice(self.colors))
        self.brick_list.append(brick)
        self.brick_cords.append([x,y])

    #check if ball at the given (x,y) position collided with any of the bricks
    def did_brick_collide(self,x,y):
        if y >= 30:
            for i in range(len(self.brick_list)): #check every brick
                cord = self.brick_cords[i]
                if abs(cord[0] - x) < 50 and abs(cord[1] - y) < 30: #condition for collision
                    self.brick_list[i].goto(500,500) #clears object out of screen
                    self.brick_cords.pop(i)
                    self.brick_list.pop(i)
                    if abs(cord[0] - x) > 45:
                        return 1 #sideway collision
                    else:
                        return 2 #vertical collision
        return 0 #no collision



