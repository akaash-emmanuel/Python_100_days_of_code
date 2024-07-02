from turtle import Turtle


POSITIONS = [(0,0), (-20,0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 0
RIGHT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()                                 # creating snake body
            new_segment.goto(position)
            self.segments.append(new_segment)
            self.add_segment(position)

    def move(self):
        for seg in range(len(self.segments)-1, 0, -1):     # (start, stop , step)
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()            # making sure the next segment goes to the position of the previous segment
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()                                 # creating snake body
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())