import colorgram
import turtle as t
import random

colors = colorgram.extract("hirst_dots.jpg", 1536)
colors_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    color_tuple = (r, g, b)
    colors_list.append(color_tuple)

t.colormode(255)
painting = t.Turtle()
painting.pensize(20)
painting.shape("circle")

painting_width = (50 * 9)# (20 * 10) + (50 * 9)
painting_height = painting_width

starting_x = -0.5 * painting_width
starting_y = -0.5 * painting_height
ending_x = 0.5 * painting_width
ending_y = 0.5 * painting_height
current_x = starting_x
current_y = starting_y

painting.teleport(starting_x, starting_y)

painting.penup()
for y in range(10):
    for x in range(10):
        color = random.choice(colors_list)
        painting.color(color)
        painting.stamp()
        painting.forward(50)
        if x != 9:
            current_x += 50
    if y != 9:
        current_x = starting_x
        current_y += 50

    painting.teleport(current_x, current_y)

screen = t.Screen()
# screen.screensize(1200,1000)
screen.exitonclick()
