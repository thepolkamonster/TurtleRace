#quiz game
from turtle import Turtle,Screen
import random
balthazar=Turtle()
screen=Screen()
# for x in range(0,25):
    #balthazar.forward(4)
    #balthazar.penup()
    #balthazar.forward(4)
    #balthazar.pendown()

dir=list(range(0,359))
len=list(range(0,5))
balthazar.speed(1000)
while(True):
    balthazar.setheading(random.choice(dir))
    balthazar.forward(random.choice(len))
screen.exitonclick()
