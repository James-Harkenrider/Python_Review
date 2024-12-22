from turtle import Turtle
SPEED = 10


class TurtleCrosser(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.reset_turtle()

    def move_up(self):
        self.forward(SPEED)

    def move_back(self):
        self.forward(-1*SPEED)

    def reset_turtle(self):
        self.goto(0, -250)
