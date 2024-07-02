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

# drawing random walk 

directions = [0, 90, 180, 270]
for _ in range(1000):
    timmy.pensize(10)   #width 
    timmy.speed("fastest")  #increases speed
    timmy.forward(20)   
    timmy.setheading(random.choice(directions))   #setheading chooses by how many degrees should turtle move, essentially randomizing directions
    timmy.color(random.choice(turtle_colors))

screen = Screen()
screen.exitonclick()