import turtle as t
from functools import partial
import random

timmy = t.Turtle()
t.colormode(255)
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red", "green")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# for _ in range (20):
#     timmy.forward(10)
#     timmy.up()
#     timmy.forward(10)
#     timmy.down()

# sides = [3, 4, 5, 6, 7, 8, 9]
# for side in sides:
#     angle = 360 / side
#     for length in range(side):
#         timmy.forward(100)
#         timmy.right(angle)

# colours = ["CornflowerBlue",
#            "DarkOrchid",
#            "IndianRed",
#            "DeepSkyBlue",
#            "LightSeaGreen",
#            "wheat",
#            "SlateGray",
#            "SeaGreen"]
# timmy.width(10)
# turtle_moves = [partial(timmy.forward, 0),
#                 partial(timmy.backward, 0),
#                 partial(timmy.right, 90),
#                 partial(timmy.left, 90)]
#
# while True:
#     timmy.pencolor(random.choice(colours))
#     random.choice(turtle_moves)()
#     timmy.forward(20)


def create_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


draw_color = create_color()
timmy.pencolor(draw_color)
timmy.speed("fastest")
heading = 0
circles = 1000
for _ in range(circles):
    draw_color = create_color()
    timmy.pencolor(draw_color)
    timmy.setheading(heading)
    timmy.circle(100)
    heading += 360/circles

screen = t.Screen()
screen.exitonclick()
