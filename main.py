# from turtle import Turtle, Screen
# from paddle import Paddle
# from ball import Ball
# from scoreboard import Scoreboard
# import time
#
# screen = Screen()
# screen.setup(width=800, height=600)
# screen.bgcolor("black")
# screen.title("Pong")
# screen.listen()
# screen.tracer(0)
#
# r_paddle = Paddle((350, 0))
# l_paddle = Paddle((-350, 0))
# is_game_on = True
#
# ball = Ball()
#
# screen.onkey(fun=r_paddle.move_up, key="Up")
# screen.onkey(fun=r_paddle.move_down, key="Down")
# screen.onkey(fun=l_paddle.move_up, key="w")
# screen.onkey(fun=l_paddle.move_down, key="s")
#
# scoreboard = Scoreboard()
#
# while is_game_on:
#     time.sleep(ball.ball_speed)
#     screen.update()
#     ball.ball_movement()
#
#     # Detects collision with top or bottom wall:
#     if ball.ycor() > 280 or ball.ycor() < -280:
#         # need to bounce
#         ball.bounce_y()
#
#     # Detect collision with paddle:
#
#     if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
#         ball.bounce_x()
#         ball.ball_speed *= 0.9
#
#     # When right paddle misses the ball:
#     if ball.xcor() > 390:
#         ball.reset_position()
#         ball.ball_speed = 0.1
#         scoreboard.l_point()
#
#     # When left paddle misses the ball:
#     if ball.xcor() < -390:
#         ball.reset_position()
#         ball.ball_speed = 0.1
#         scoreboard.r_point()
#
# screen.exitonclick()

import pygame
import time

pygame.init()
# Game constants
WIDTH = 1000
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
fps = 60
timer = pygame.time.Clock()
# Credits:
# Icon: <a href="https://www.flaticon.com/free-icons/ping-pong" title="ping pong icons">Ping pong icons created by Freepik - Flaticon</a>
# Design of screen:
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Icon:
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Game variables:
paddle1_y = 250
paddle2_y = 250
paddle1_y_change = 0
paddle2_y_change = 0


def paddle(x, y):
    pygame.draw.rect(screen, WHITE, [x, y, 20, 20])


running = True
while running:
    timer.tick(fps)
    screen.fill(BLACK)

    paddle1 = paddle(950, paddle1_y)
    paddle2 = paddle(30, paddle2_y)

    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                paddle1_y_change -= 5
            if event.key == pygame.K_DOWN:
                paddle1_y_change += 5
            if event.key == pygame.K_w:
                paddle2_y_change -= 5
            if event.key == pygame.K_s:
                paddle2_y_change += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                paddle1_y_change = 0
            if event.key == pygame.K_DOWN:
                paddle1_y_change = 0
            if event.key == pygame.K_w:
                paddle2_y_change = 0
            if event.key == pygame.K_s:
                paddle2_y_change = 0

    paddle1_y += paddle1_y_change
    paddle2_y += paddle2_y_change

    pygame.display.flip()
pygame.quit()
