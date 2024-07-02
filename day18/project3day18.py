from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("arrow")
turtle_colors = [
    "red", "blue", "green", "yellow", "orange", "purple", "pink",
    "brown", "black", "gray", "cyan", "magenta", "gold",
    "silver", "indigo", "violet", "turquoise", "coral", "lightblue",
    "lightgreen", "lightyellow", "lightpink", "darkblue", "darkgreen",
    "darkred", "darkorange", "darkviolet", "darkcyan", "maroon",
    "navy", "olive", "teal", "lime", "aquamarine", "azure", "beige",
    "bisque", "chocolate", "crimson", "fuchsia", "ivory", "khaki",
    "lavender", "orchid", "peachpuff", "plum", "salmon", "seagreen",
    "sienna", "skyblue", "slateblue", "springgreen", "tan", "thistle",
    "tomato", "wheat"
]

# draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon, .......
def draw_shape(number_of_sides):
    angle = 360/number_of_sides
    for _ in range(number_of_sides):
        timmy.forward(100)
        timmy.right(angle)
for _ in range(3,101):
    timmy.color(random.choice(turtle_colors))
    draw_shape(_)

screen = Screen()
screen.exitonclick()