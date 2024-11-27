from turtle import Turtle


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.color("yellow")
        self.goto(0, 300)
        self.pendown()
        self.right(90)
        while self.ycor() > -300:
            self.forward(5)
            self.penup()
            self.forward(5)
            self.pendown()
        self.hideturtle()
