import pygame
import time
from turtle import Screen, Turtle

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard, FONT

screen = Screen()
screen.title("Turtle_Race_Game")
screen.setup(width=600, height=600)
screen.tracer(0)
pygame.init()

turtle = Turtle()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()


def move(direction):
    player.move(direction)


def enter_name(name):
    """prompt to ask player's name"""
    turtle.penup()
    turtle.goto(250, 260)
    turtle.write(f"{name}", align="right", font=FONT)
    turtle.hideturtle()


name = input("Please enter your name! ")
enter_name(name)
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
            game_is_on = False
            scoreboard.game_over(scoreboard.level, name)

    # Detect if the turtle successfully cross the road
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

pygame.mixer.music.stop()
screen.exitonclick()
