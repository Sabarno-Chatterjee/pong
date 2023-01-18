from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed(0)
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def ball_movement(self):
        x_position = self.xcor() + self.x_move
        y_position = self.ycor() + self.y_move
        self.goto(x=x_position, y=y_position)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def new_ball_movement(self, x_position):
        x_direction = x_position * -1
        self.goto(x=x_direction)

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
