from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("gold")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-13, 13)
        random_x *= 20
        random_y = random.randint(-13, 13)
        random_y *= 20
        self.goto(x=random_x, y=random_y)
