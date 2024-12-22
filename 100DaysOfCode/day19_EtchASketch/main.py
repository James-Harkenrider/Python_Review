import turtle
from turtle import Turtle, Screen


class EtchASketch:

    def __init__(self):
        self.cursor = Turtle()
        self.screen = Screen()
        self.heading = 0
        self.x, self.y = self.cursor.position()

    def forward(self):
        self.cursor.forward(10)

    def backwards(self):
        self.cursor.backward(10)

    def clockwise(self):
        self.heading += 10
        self.cursor.setheading(self.heading)

    def counter_clockwise(self):
        self.heading -= 10
        self.cursor.setheading(self.heading)

    def clear_screen(self):
        self.cursor.clear()
        self.cursor.teleport(self.x, self.y)

    def call_move(self):
        self.screen.listen()
        self.screen.onkey(self.forward, "w")
        self.screen.onkey(self.backwards, "s")
        self.screen.onkey(self.clockwise, "a")
        self.screen.onkey(self.counter_clockwise, "d")
        self.screen.onkey(self.clear_screen, "c")
        self.screen.exitonclick()


practice = EtchASketch()
practice.call_move()
