from turtle import *
from random import randint
speed(100)
bgcolor("BLACK")
x=1
while x<400:
    aqua=randint(0,255)
    blue=randint(0,255)
    cyan2=randint(0,238)
    colormode(255)
    pencolor(aqua,blue,cyan2)
    forward(75+x)
    right(90.911)
    x=x+1
exitonclick()
