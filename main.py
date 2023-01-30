import random

import pygame
import math
from pygame import mixer

pygame.init()
# Game constants
WIDTH = 1000
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
fps = 60
timer = pygame.time.Clock()
# Credits:
#
# Design of screen:
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Icon:
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Game variables:
paddle1_y = 250
paddle2_y = 250
paddle1_x = 950
paddle2_x = 30
paddle1_y_change = 0
paddle2_y_change = 0
game_ball_X = 492
game_ball_Y = 292
game_ball_X_change = -4
game_ball_Y_change = 4
paddle1_score = 0
paddle2_score = 0
font = pygame.font.Font('freesansbold.ttf', 50)

# Background image:
backgroundImg = pygame.image.load("board.png")
# Ball image:
ballImg = pygame.image.load("ball.png")


def distance(ball_x, ball_y, paddles_x, paddles_y):
    return math.sqrt(math.pow(ball_x - paddles_x, 2) + math.pow(ball_y - paddles_y, 2))


def sound():
    audio = mixer.Sound("bounce.wav")
    audio.play()


running = True
while running:
    timer.tick(fps)
    screen.fill(BLACK)
    screen.blit(backgroundImg, (0, 0))

    paddle1 = pygame.draw.rect(screen, WHITE, pygame.Rect(paddle1_x, paddle1_y, 10, 120), 5, 5, 5, 5)
    paddle2 = pygame.draw.rect(screen, WHITE, pygame.Rect(paddle2_x, paddle2_y, 10, 120), 5, 5, 5, 5)
    screen.blit(ballImg, (game_ball_X, game_ball_Y))
    score1 = font.render(str(paddle1_score), True, WHITE)
    screen.blit(score1, (700, 30))
    score2 = font.render(str(paddle2_score), True, WHITE)
    screen.blit(score2, (300, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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

    # Paddle movements:
    paddle1_y += paddle1_y_change
    paddle2_y += paddle2_y_change

    # Game ball movements:
    game_ball_X += game_ball_X_change
    game_ball_Y += game_ball_Y_change
    if game_ball_Y <= 12 or game_ball_Y >= 588:
        game_ball_Y_change = game_ball_Y_change * -1
    elif game_ball_X <= 12:
        paddle1_score += 1
        game_ball_Y = 292
        game_ball_X = 492
        game_ball_X_change = -4
        game_ball_X_change = game_ball_X_change * -1
    elif game_ball_X >= 988:
        paddle2_score += 1
        game_ball_Y = 292
        game_ball_X = 492
        game_ball_X_change = -4
        game_ball_X_change = game_ball_X_change * -1

    # Collision with paddles:

    collision1 = distance(game_ball_X, game_ball_Y, paddle1_x, paddle1_y)
    if collision1 < 100 and game_ball_X > 925:
        sound()
        game_ball_X_change = game_ball_X_change * -1.1

    collision2 = distance(game_ball_X, game_ball_Y, paddle2_x, paddle2_y)
    if collision2 < 100 and game_ball_X < 45:
        sound()
        game_ball_X_change = game_ball_X_change * -1

    if paddle1_y >= 480:
        paddle1_y = 480
    elif paddle1_y <= 0:
        paddle1_y = 0
    # Paddle2 position:
    if paddle2_y >= 480:
        paddle2_y = 480
    elif paddle2_y <= 0:
        paddle2_y = 0
    if game_ball_X < 700:
        if random.randint(0, 5) == 1:
            if game_ball_Y >= 0 and game_ball_Y <= 100:
                paddle2_y = 0
            elif game_ball_Y >= 100 and game_ball_Y <= 200:
                paddle2_y = 120
            elif game_ball_Y >= 200 and game_ball_Y <= 300:
                paddle2_y = 220
            elif game_ball_Y >= 300 and game_ball_Y <= 400:
                paddle2_y = 320
            elif game_ball_Y >= 400 and game_ball_Y <= 500:
                paddle2_y = 420
            elif game_ball_Y >= 500 and game_ball_Y <= 590:
                paddle2_y = 480

    # To automate both paddles:
    # if game_ball_X > 300:
    #     if game_ball_Y >= 0 and game_ball_Y <= 100:
    #         paddle1_y = 0
    #     elif game_ball_Y >= 100 and game_ball_Y <= 200:
    #         paddle1_y = 120
    #     elif game_ball_Y >= 200 and game_ball_Y <= 300:
    #         paddle1_y = 220
    #     elif game_ball_Y >= 300 and game_ball_Y <= 400:
    #         paddle1_y = 320
    #     elif game_ball_Y >= 400 and game_ball_Y <= 500:
    #         paddle1_y = 420
    #     elif game_ball_Y >= 500 and game_ball_Y <= 590:
    #         paddle1_y = 480

    if collision2 < 100 and game_ball_X < 45:
        sound()
        paddle2_y_change = 0
        paddle2_y = 250
    pygame.display.flip()
pygame.quit()