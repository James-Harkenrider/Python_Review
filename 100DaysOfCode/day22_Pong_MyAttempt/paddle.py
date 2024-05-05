from turtle import Turtle
PADDLE_SIZE = 4
PADDLE_X = 550
MOVE_SPEED = 15


class Paddle(Turtle):

    def __init__(self, player_side="right"):
        super().__init__()
        self.paddle_size = PADDLE_SIZE
        self.player_side = player_side
        self.paddle_x = self.find_side()
        self.paddle_y = 0
        self.paddle_segments = []
        self.create_paddle()

    def find_side(self):
        if self.player_side.lower() == "left":
            return PADDLE_X * -1
        return PADDLE_X

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(self.paddle_x, self.paddle_y)

    def up(self):
        if self.ycor() > 280:
            return
        current_y = self.ycor()
        self.goto(self.paddle_x, current_y + MOVE_SPEED)

    def down(self):
        if self.ycor() < -280:
            return
        current_y = self.ycor()
        self.goto(self.paddle_x, current_y - MOVE_SPEED)
