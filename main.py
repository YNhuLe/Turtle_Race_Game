import pygame
import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle_Race_Game")
screen.setup(width=600, height=600)
screen.tracer(0)
pygame.init()

player = Player()
car_manager = CarManager()

screen.listen()


def move(direction):
    player.move(direction)


# Map keys corresponding directions
key_directions = {"Left": "left", "Right": "right", "Up": "up", "Down": "down"}

for key, direction in key_directions.items():
    screen.onkey(lambda dir=direction: move(dir), key)

game_is_on = True
pygame.mixer.init()
pygame.mixer.music.load('Puppy_Love.mp3')
pygame.mixer.music.play(-1)
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # Detect the collision of the turtle with the cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:

            player.game_over_notification()
            game_is_on = False

    # Detect if the turtle successfully cross the road
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()

pygame.mixer.music.stop()
screen.exitonclick()
