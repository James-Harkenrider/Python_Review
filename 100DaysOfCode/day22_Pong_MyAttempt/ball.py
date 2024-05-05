from turtle import Turtle
SPEED = 15


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x_move = SPEED
        self.y_move = SPEED

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0,0)
        self.x_move *= -1
        self.y_move *= -1