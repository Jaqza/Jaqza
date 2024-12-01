from turtle import Turtle
from random import choice


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.randoms = [-6, -5, -4, -3, 3, 4, 5, 6]
        self.x_move = choice(self.randoms)
        self.y_move = choice(self.randoms)
        self.velocity = 0.06

    def velocity_up(self):
        self.velocity *= 0.8
        return self.velocity

    def ball_restart(self):
        self.teleport(0, 0)
        self.velocity = 0.06
        self.bounce_x()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
