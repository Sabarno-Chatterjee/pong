from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
is_game_on = True

ball = Turtle(shape = "circle")
ball.color("white")
ball.penup()
ball.shapesize(stretch_len=1, stretch_wid=1)

screen.onkey(fun=paddle1.move_up, key="Up")
screen.onkey(fun=paddle1.move_down, key="Down")
screen.onkey(fun=paddle2.move_up, key="w")
screen.onkey(fun=paddle2.move_down, key="s")

while is_game_on:
    screen.update()

screen.exitonclick()
