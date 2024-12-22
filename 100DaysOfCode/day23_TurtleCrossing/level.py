from turtle import Turtle


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.level = 0
        self.goto(-280, 270)
        self.new_level()

    def new_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Courier", 15, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align="center", font=("Courier", 15, "normal"))