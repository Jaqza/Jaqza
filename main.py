from turtle import Screen
from net import Net
from planks import PlayerPlank
import time
from ball import Ball
from scoreboards import Scoreboard


def speed_up(starting_speed):
    starting_speed *= 0.9
    return starting_speed
# Screen settings


screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.bgcolor("gray")
screen.tracer(0)
# Objects
ball = Ball()
right_board = PlayerPlank((280, 0))
left_board = PlayerPlank((-280, 0))
net = Net()
scoreboard = Scoreboard()
# Commands
screen.onkey(left_board.move_up, "w")
screen.onkey(left_board.move_down, "s")
screen.onkey(right_board.move_up, "Up")
screen.onkey(right_board.move_down, "Down")
# Logic
is_game_on = True

while is_game_on:

    ball.move()
    screen.update()
    time.sleep(ball.velocity)
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()
    if ball.distance(left_board) < 65 and ball.xcor() == -280:
        ball.bounce_x()
        ball.velocity_up()
    if ball.distance(right_board) < 65 and ball.xcor() == 280:
        ball.bounce_x()
        ball.velocity_up()
    if ball.xcor() > 310:
        scoreboard.left_add_point()
        ball.ball_restart()
    if ball.xcor() < -310:
        scoreboard.right_add_point()
        ball.ball_restart()
screen.exitonclick()
