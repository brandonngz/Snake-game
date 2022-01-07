from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_segment = Turtle(shape="square")
        snake_segment.penup()
        # snake_segment.shapesize(stretch_len=0.5, stretch_wid=0.5)
        snake_segment.color("white")
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def extend_snake(self):
        # Add a new segment to the snake
        self.add_segment(self.segments[len(self.segments) - 1].position())

    def move(self):
        for seg_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

# Arrow Key-words
    def up(self):
        if self.head.heading() != DOWN:
            #                    90
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            #                    270
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            #                    180
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            #                     0
            self.head.setheading(RIGHT)

