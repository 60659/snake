import time
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.speed("fastest")
        self.color("white")
        self.goto(x=0, y=270)
        self.hideturtle()
        self.score = 0
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.clear()
        self.score += 1
        self.goto(x=0, y=270)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("gold")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
