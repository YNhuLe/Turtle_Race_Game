from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown"]
STARTING_MOVE_DISTANCE = 5
MOVE_DISTANCE = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """This method create the car in random colors and with random position in the right hand-side of the screen"""
        random_chance = random.randint(1, 6)  # given the random chance from 1 to 6
        if random_chance == 1:  # when the random number is 1 => a car will be created
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            """Move the cars from the right hand-side of the screen to the left hand-side"""
            car.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        """Speed up the cars when the turtle level up"""
        self.car_speed += MOVE_DISTANCE
