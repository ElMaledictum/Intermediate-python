from turtle import Turtle, position

STARTING_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.body = []
        self.create_snake()
        self.snakehead = self.body[0]

    def create_snake(self):
        # creates the first 3 segments of the snake
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, pos):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.shapesize(0.5, 0.5, 1)
        segment.penup()
        segment.goto(pos)
        self.body.append(segment)

    def grow(self):
        # adds another segment to the last element in the "head" list
        self.add_segment(self.body[-1].position())

    def move(self):
        # makes the last segment go to the 2nd to the last position
        # and so on...
        for seg_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(new_x, new_y)
        self.snakehead.forward(MOVE_DISTANCE)

    def up(self):
        if self.snakehead.heading() != DOWN:
            self.snakehead.setheading(UP)

    def down(self):
        if self.snakehead.heading() != UP:
            self.snakehead.setheading(DOWN)

    def right(self):
        if self.snakehead.heading() != LEFT:
            self.snakehead.setheading(RIGHT)

    def left(self):
        if self.snakehead.heading() != RIGHT:
            self.snakehead.setheading(LEFT)

    def reset(self):
        for each_seg in self.body:
            each_seg.goto(1000, 1000)
        self.body.clear()    
        self.create_snake()
        self.snakehead = self.body[0]
