from turtle import Screen, Turtle
from dashed_line import DashedLine
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Setup Screen
screen = Screen()
screen.tracer(0)
screen.setup(height=700, width=1200)
screen.bgcolor("black")

# Add divide between player zones
center_line = DashedLine()
center_line.draw_line()

paddle_left = Paddle(player_side="left")
paddle_right = Paddle(player_side="right")
pong_ball = Ball()
score = Scoreboard()
screen.update()

screen.listen()
screen.onkeypress(paddle_left.up, 'w')
screen.onkeypress(paddle_left.down, 's')
screen.onkeypress(paddle_right.up, 'Up')
screen.onkeypress(paddle_right.down, 'Down')

game_is_on = True
while game_is_on:
    # Detect wall collision
    if pong_ball.ycor() > 330 or pong_ball.ycor() < -310:
        pong_ball.bounce_y()
    # Detect paddle collision
    if pong_ball.distance(paddle_right) < 50 and pong_ball.xcor() > 520 or \
       pong_ball.distance(paddle_left) < 50 and pong_ball.xcor() < -520:

        pong_ball.bounce_x()

    # Keep score of game
    if pong_ball.xcor() > 600:
        pong_ball.reset()
        score.add_l_score()
    elif pong_ball.xcor() < -600:
        pong_ball.reset()
        score.add_r_score()

    screen.update()
    pong_ball.move()
    time.sleep(0.1)

screen.exitonclick()
