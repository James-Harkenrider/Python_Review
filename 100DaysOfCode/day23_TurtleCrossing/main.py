from turtle import Screen
from turtle_crosser import TurtleCrosser
from car import Car
from level import Level
import time
CAR_LIMIT = 6

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create turtle object and list for car objects
tim = TurtleCrosser()
display_level = Level()
cars = []

# Controls for turtle
screen.listen()
screen.onkey(tim.move_up, "Up")
screen.onkey(tim.move_back, "Down")

# Begin playing game
game_on = True
car_limiter = 0
while game_on:
    screen.update()
    time.sleep(0.1)

    # Control number of cars on board, higher number means fewer cars
    if car_limiter == CAR_LIMIT:
        new_car = Car()
        cars.append(new_car)
        car_limiter = 0

    # Move each car object on board, delete cars that are off board
    car_index = 0
    for car in cars:
        car.drive()
        # Detect car collision
        if car.distance(tim) < 25:
            display_level.game_over()
            game_on = False
        if car.xcor() < -350:
            del cars[car_index]
        car_index += 1

    # Detect level completion
    if tim.ycor() > 280:
        display_level.new_level()
        tim.reset_turtle()
        for car in cars:
            car.increase_speed()
        time.sleep(3)

    car_limiter += 1

screen.exitonclick()
