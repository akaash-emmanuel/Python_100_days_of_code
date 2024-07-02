from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("arrow")

# draw a dashed line
for _ in range(10):
    timmy.forward(5)
    timmy.penup()
    timmy.forward(5)
    timmy.pendown()

screen = Screen()
screen.exitonclick()