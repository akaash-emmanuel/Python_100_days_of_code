from turtle import Screen
import turtle as t
import random

timmy = t.Turtle()
timmy.shape("arrow")
t.colormode(255)            #changing color mode so it accepts rgb tuples instead of a string

# drawing a spirograph

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

timmy.speed("fastest")
def spirograph(size):
    for _ in range(int(360/size)):
        timmy.color(random_color())
        timmy.circle(100)   #drawing one circle
        timmy.setheading(timmy.heading() + size)          # tilting the turtle by adding a few degrees to the variable and setting it using setheading
spirograph(1)

screen = Screen()
screen.exitonclick()