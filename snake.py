from turtle import Turtle

STARTING_POSITIONS = [(-20, 0), (-40, 0), (-60, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):

        self.segments = []
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        self.head = self.segments[0]
        self.head.color("gold")

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.up()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)
