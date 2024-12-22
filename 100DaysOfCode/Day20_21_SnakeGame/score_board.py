from turtle import Turtle
FONT = ('courier', 12, 'normal')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", align='center', font=FONT)

    def score_counter(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align='center', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align='center', font=FONT)
