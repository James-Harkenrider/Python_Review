from turtle import Turtle
import random
COLORS = ["green", "blue", "purple", "orange", "yellow", "red"]


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2.5)
        self.penup()
        self.setheading(180)
        self.random_location()
        self.speed = 10
        self.color(random.choice(COLORS))

    def random_location(self):
        self.goto(random.randint(350, 450), random.randint(-200, 280))

    def drive(self):
        self.forward(self.speed)

    def increase_speed(self):
        self.speed += 2
