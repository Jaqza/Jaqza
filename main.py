from turtle import Turtle, Screen
from net import Net
from board import PlayerBoard
import time
from my_workspace import Ball

"""Screen settings"""
screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
"""Objects"""
right_board = PlayerBoard((280, 0))
left_board = PlayerBoard((-280, 0))
net = Net()
ball = Ball()

"""Stering"""
screen.onkey(left_board.move_up,"w")
screen.onkey(left_board.move_down,"s")
screen.onkey(right_board.move_up,"Up")
screen.onkey(right_board.move_down,"Down")
"""Logic"""


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.04)
    ball.move()

    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()
    if ball.distance(left_board) < 50 and ball.xcor() == -270:
        ball.bounce_x()
    if ball.distance(right_board) < 50 and ball.xcor() == 270:
        ball.bounce_x()
    if ball.xcor() > 310 or ball.xcor() < -310:
        ball.teleport(0, 0)
        screen.update()
        time.sleep(1)
        ball.bounce_x()



















screen.exitonclick()