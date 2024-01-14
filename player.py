from turtle import Turtle

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

    def go_up(self):
        """Tell the turtle to go up """
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """Get the player to back to the starting position"""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Check if the turtle getting close to the finish line on top of the screen"""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
