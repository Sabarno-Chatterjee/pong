# from turtle import Turtle
#
#
# class Paddle(Turtle):
#     def __init__(self, position):
#         super().__init__()
#         self.shape("square")
#         self.color("white")
#         self.penup()
#         self.speed("fastest")
#         self.shapesize(stretch_wid=5, stretch_len=1)
#         self.goto(position)
#
#     def move_up(self):
#         y_position = self.ycor() + 20
#         self.goto(x=self.xcor(), y=y_position)
#
#     def move_down(self):
#         y_position = self.ycor() - 20
#         self.goto(x=self.xcor(), y=y_position)
import pygame

