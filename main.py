from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)


# def move_up():
#     y_position = paddle.ycor() + 20
#     paddle.goto(x=paddle.xcor(),y=y_position)
#
#
# def move_down():
#     y_position = paddle.ycor() - 20
#     paddle.goto(x=paddle.xcor(),y=y_position)

# screen.onkey(fun=move_up, key="Up")
# screen.onkey(fun=move_down, key="Down")

paddle1 = Paddle(350, 0)
paddle2 = Paddle(-350, 0)

is_game_on = True

while is_game_on:
    screen.update()



screen.exitonclick()
