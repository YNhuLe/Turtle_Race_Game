from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        """update the level on the scoreboard and clear the level everytime the new
        level updated"""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """increase the level everytime the turtle cross the screen successfully"""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """pop up the game over when the turtle hit the car"""
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
