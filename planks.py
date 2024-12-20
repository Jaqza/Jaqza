from turtle import Turtle


class PlayerPlank(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        x_cord = self.xcor()
        y_cord = self.ycor()
        self.goto((x_cord, y_cord + 35))

    def move_down(self):
        x_cord = self.xcor()
        y_cord = self.ycor()
        self.goto((x_cord, y_cord - 35))
