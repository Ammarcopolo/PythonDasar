import turtle as t
import math 
from turtle import *

t.speed(10)
t.tracer(10)

def hearta (k):
    return 15*math.sin(k)**3
def heartb(k):
    return 12*math.cos(k)-5*\
        math.cos(2*k)-2*\
        math.cos(3*k)-\
        math.cos(4*k)

def txt():
    pen.up()
    pen.setpos(-68, 95)
    pen.down()
    pen.color('lightgreen')
    pen.write('I Love You', font=("Verdana", 12, "bold"))

speed(100)
bgcolor("black")
for i in range(600):
    goto(hearta(i)*20,heartb(i)*20)
    for j in range(5):
        color("#f73487")
    goto(0,0)

txt()
turtle.done()