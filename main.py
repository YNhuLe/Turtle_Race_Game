import pygame
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
pygame.init()

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

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

    if player.is_at_finish_line():
        player.go_to_start()

pygame.mixer.music.stop()
screen.exitonclick()
