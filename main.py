from ball import Ball
from bricks import Brickery
from paddle import Paddle
from scoreboard import Scoreboard
from turtle import Screen
import time

##### Screen specifications #####
WIDTH = 800
HEIGHT = 600
UPPER_BOUND = 280
LOWER_BOUND = -280
RIGHT_BOUND = 400
LEFT_BOUND = -400

##### Set up screen window #####
screen = Screen()
screen.setup(width=WIDTH,height=HEIGHT)
screen.bgcolor("black")
screen.title("Atari Blackout Game, but full of bugs. by Jh :)")
screen.tracer(0)

##### Bind mouse to screen #####
canvas = screen.getcanvas()
mouse_x = 0
def set_coords(event):
    global mouse_x
    mouse_x = event.x
canvas.bind('<Motion>', set_coords) #bind event '<Motion>' to trigger the function set_coords

##### Create screen objects #####
paddle = Paddle(0, -200)
ball = Ball()
scoreboard = Scoreboard()
brickery = Brickery()
for r in range(3):
    for c in range(6):
        brickery.make_brick(-300 + 120*c, 50*r + 50)
all_bricks = brickery.brick_list

# ##### Bind key press to object & function #####
# screen.listen()
# screen.onkeypress(paddle.left, "Left")
# screen.onkeypress(paddle.right, "Right")

##### Main program for gameplay #####
game_on = True
speed = 10
while game_on:
    #adjust frames per second
    time.sleep(0.05)
    screen.update()

    #ball & paddle movement
    ball.move(speed)
    paddle.goto(mouse_x - 350, -200)

    #check for ball-paddle collisions
    if abs(ball.ycor()+200) < 25:
        if abs(paddle.xcor() - ball.xcor() - 60) <= 40: #same as 100 >= paddle.xcor() - ball.xcor() >= 20
            ball.paddle_bounce_l()
            speed += 2
        elif abs(ball.xcor() - paddle.xcor() - 60) <= 40: #same as 100 >= ball.xcor() - paddle.xcor() >= 20
            ball.paddle_bounce_r()
            speed += 2
        elif abs(ball.xcor() - paddle.xcor()) < 20:
            ball.paddle_bounce_c()
            speed += 2
        else:
            pass

    #check for ball-brick collisions
    collision_code = brickery.did_brick_collide(ball.xcor(), ball.ycor())
    if collision_code != 0:
        scoreboard.add_point()
        if collision_code == 1:
            ball.h_bounce()
        else:
            ball.v_bounce()

    #check for ball-wall collisions
    if ball.ycor() >= UPPER_BOUND:
        ball.v_bounce()
    if ball.xcor() >= RIGHT_BOUND or ball.xcor() <= LEFT_BOUND:
        ball.h_bounce()

    #check if game has ended
    if ball.ycor() <= LOWER_BOUND:
        game_on = False
    if brickery.brick_list == []:
        game_on = False
        time.sleep(0.1)
        scoreboard.goto(0, 0)
        scoreboard.write(f"Congrats, you won the game! :D", align = "center", font = ("courier", 30, "normal"))

screen.exitonclick()
