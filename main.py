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

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
is_game_on = True

ball = Ball()

screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")

while is_game_on:
    time.sleep(0.09)
    screen.update()
    ball.ball_movement()

    # Detects collision with top or bottom wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        print("bounce")
        # need to bounce
        ball.bounce_y()

    # Detect collision with paddle:

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print("made contact")
        ball.bounce_x()

screen.exitonclick()
