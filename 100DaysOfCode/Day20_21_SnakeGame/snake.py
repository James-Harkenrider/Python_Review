from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20


class Snake:
    def __init__(self):
        self.seg_list = []
        self.make_snake()
        self.head = self.seg_list[0]

    def make_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        seg = Turtle(shape="square")
        seg.color("white")
        seg.penup()
        seg.goto(position)
        self.seg_list.append(seg)

    def extend(self):
        new_seg_pos = (self.seg_list[-1].xcor(), self.seg_list[-1].ycor())
        self.add_segment(new_seg_pos)

    def move(self):
        for seg in range((len(self.seg_list)-1), 0, -1):
            new_x = self.seg_list[seg - 1].xcor()
            new_y = self.seg_list[seg - 1].ycor()
            self.seg_list[seg].goto(new_x, new_y)
        self.head.forward(MOVE)

    def up(self):
        heading = self.head.heading()
        if heading == 0:
            self.head.left(90)
        elif heading == 180:
            self.head.right(90)

    def down(self):
        heading = self.head.heading()
        if heading == 0:
            self.head.right(90)
        elif heading == 180:
            self.head.left(90)

    def right(self):
        heading = self.head.heading()
        if heading == 90:
            self.head.right(90)
        elif heading == 270:
            self.head.left(90)

    def left(self):
        heading = self.head.heading()
        if heading == 90:
            self.head.left(90)
        elif heading == 270:
            self.head.right(90)
