from turtle import Screen
from net import Net
from planks import PlayerPlank
import time
from ball import Ball
from scoreboards import Scoreboard


def ball_reset():
    ball.teleport(0, 0)
    screen.update()
    time.sleep(1)
    ball.bounce_x()
# Screen settings


screen = Screen()


screen.listen()
screen.setup(width=600, height=600)
screen.bgcolor("gray")
screen.tracer(0)
# Objects
right_board = PlayerPlank((280, 0))
left_board = PlayerPlank((-280, 0))
net = Net()
ball = Ball()
scoreboard = Scoreboard()
# Commands
screen.onkey(left_board.move_up, "w")
screen.onkey(left_board.move_down, "s")
screen.onkey(right_board.move_up, "Up")
screen.onkey(right_board.move_down, "Down")
# Logic
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
    if ball.xcor() > 310:
        ball_reset()
        scoreboard.left_add_point()
    if ball.xcor() < -310:
        ball_reset()
        scoreboard.right_add_point()
screen.exitonclick()
