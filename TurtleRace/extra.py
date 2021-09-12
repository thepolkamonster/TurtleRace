import random
from turtle import Turtle, Screen
import turtle

t = Turtle()
screen = Screen()
turtle.colormode(255)


def color_choice():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    res = (r, g, b)
    return res


t.speed('fastest')
for x in range(360):
    # choice = random.choice(colors)
    t.color(color_choice())
    t.circle(100)
    t.left(1)
screen.exitonclick()
# i cant make random colors

