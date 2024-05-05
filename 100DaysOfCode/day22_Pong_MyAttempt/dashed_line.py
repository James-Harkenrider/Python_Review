from turtle import Turtle
POINTER_START = 345


class DashedLine:

    def __init__(self):
        self.pointer_location = POINTER_START

    def draw_line(self):
        segment = Turtle(shape="square")
        segment.shapesize(0.25)
        segment.color("white")
        segment.penup()
        # Draw line until we reach bottom of screen
        while self.pointer_location > -1 * POINTER_START:
            # Each dash will be three squares long
            for _ in range(3):
                segment.goto(0, self.pointer_location)
                segment.stamp()
                self.pointer_location -= 5

            self.pointer_location -= 15
