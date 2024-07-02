import turtle as t
import random

t.colormode(255)
timmy = t.Turtle()
color_list = [(9, 18, 38), (185, 167, 126), (119, 95, 70), (230, 223, 188), (67, 90, 105), (48, 31, 41), (213, 199, 153), (78, 101, 91), (24, 49, 41), (155, 137, 82), (152, 165, 156), (97, 72, 80), (58, 41, 31), (208, 215, 209), (209, 216, 222), (142, 159, 175), (53, 60, 81), (82, 53, 63), (41, 72, 80), (45, 74, 66), (75, 73, 37), (89, 52, 46), (98, 124, 167), (115, 136, 124), (165, 113, 95), (186, 196, 186), (108, 135, 140), (184, 190, 202), (168, 162, 165), (207, 204, 206), (185, 194, 196), (151, 109, 114), (196, 190, 189), (195, 190, 191)]
timmy.penup()
timmy.hideturtle()
timmy.setheading(255)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100
timmy.speed("fastest")


for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen = t.Screen()
screen.exitonclick()
