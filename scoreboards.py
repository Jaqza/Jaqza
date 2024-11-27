from turtle import Turtle


class Scoreboard:

    def __init__(self):
        self.left_score = -1
        self.right_score = -1
        self.left_scoreboard = Turtle()
        self.right_scoreboard = Turtle()
        self.create_left_scoreboard()
        self.create_right_scoreboard()
        self.right_add_point()
        self.left_add_point()

    def create_left_scoreboard(self):
        self.left_scoreboard.teleport(-20, 280)
        self.left_scoreboard.color("blue")
        self.left_scoreboard.hideturtle()

    def create_right_scoreboard(self):
        self.right_scoreboard.teleport(20, 280)
        self.right_scoreboard.color("blue")
        self.right_scoreboard.hideturtle()

    def left_add_point(self):
        self.left_scoreboard.clear()
        self.left_score += 1
        self.write_scores()

    def right_add_point(self):
        self.right_scoreboard.clear()
        self.right_score += 1
        self.write_scores()

    def write_scores(self):
        self.left_scoreboard.write(f"{self.left_score}", False, "center", ("Courier", 16, "normal"))
        self.right_scoreboard.write(f"{self.right_score}", False, "center", ("Courier", 16, "normal"))
