from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
is_game_on = True

ball = Ball()

screen.onkey(fun=paddle1.move_up, key="Up")
screen.onkey(fun=paddle1.move_down, key="Down")
screen.onkey(fun=paddle2.move_up, key="w")
screen.onkey(fun=paddle2.move_down, key="s")

while is_game_on:
    ball.ball_movement()
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
