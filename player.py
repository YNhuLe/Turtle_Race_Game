from turtle import Turtle
from scoreboard import FONT
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def move(self, direction):
        """move the turtle to the up, down, left and right"""
        if direction == "up":
            self.forward(MOVE_DISTANCE)
        elif direction == "down":
            self.backward(MOVE_DISTANCE)
        elif direction == "left":
            x = self.xcor()
            x -= MOVE_DISTANCE
            self.setx(x)
        elif direction == "right":
            x = self.xcor()
            x += MOVE_DISTANCE
            self.setx(x)

    def go_to_start(self):
        """Get the player to back to the starting position"""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Check if the turtle getting close to the finish line on top of the screen"""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

