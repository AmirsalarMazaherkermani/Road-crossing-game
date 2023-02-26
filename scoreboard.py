from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.current_level = 1
        self.goto(-280, 250)
        self.score_text()

    def score_text(self):
        self.clear()
        self.write(f"Level :{self.current_level}", False, "left", FONT)

    def add_level(self):
        self.current_level += 1
        self.score_text()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", FONT)
