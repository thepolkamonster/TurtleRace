from turtle import Turtle, Screen

balthazar=Turtle()
balthazar.shape('turtle')
balthazar.color('purple')
for x in range(0,50):
    balthazar.back(100)
    balthazar.forward(100)

screen=Screen()
screen.exitonclick()