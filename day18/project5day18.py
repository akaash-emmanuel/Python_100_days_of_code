from turtle import Screen
import turtle as t
import random

timmy = t.Turtle()
timmy.shape("arrow")
t.colormode(255)            #changing color mode so it accepts rgb tuples instead of a string

# creating random colors instead of choosing from a list of colors

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
for _ in range(1000):
    timmy.pensize(10)   #width 
    timmy.speed("fastest")  #increases speed
    timmy.forward(20)   
    timmy.setheading(random.choice(directions))   #setheading chooses by how many degrees should turtle move, essentially randomizing directions
    timmy.color(random_color())


screen = Screen()
screen.exitonclick()