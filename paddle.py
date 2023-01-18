from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.starting_position(x_position, y_position)

    def starting_position(self, x_position, y_position):
        self.goto(x=x_position,y=y_position)





