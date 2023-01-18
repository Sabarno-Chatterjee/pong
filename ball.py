from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)

    def ball_movement(self):
        x_position = self.xcor() + 5
        y_position = self.ycor() + 5
        self.goto(x=x_position, y=y_position)
