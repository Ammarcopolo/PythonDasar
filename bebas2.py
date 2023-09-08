from turtle import *

av=Turtle()

s=Screen()

s.bgcolor("black")

av.penup()

av.setposition(-20,-350)

av.pendown()

av.begin_fill()

av.color("red")

av.circle(300)

av.end_fill()

av.penup()

av.setposition(-20,-260)

av.pendown()

av.begin_fill()

av.color("black")

av.circle(230)

av.end_fill()

av.penup()

av.setposition(0,-100)

av.pendown()

av.begin_fill()

av.color("red")

av.pensize(2)

av.pencolor("grey")

av.backward(100)

av.left(60)

av.backward(200)

av.right(60)

av.backward(85)

av.right(115)

av.backward(600)

av.right(65)

av.backward(130)

av.right(90)

av.backward(440)

av.right(90)

av.backward(100)

av.right(90)

av.backward(65)

av.end_fill()

av.penup()

av.setposition(0,-50)

av.pendown()

av.pensize(2)



av.begin_fill()

av.color("black")

av.pencolor("grey")

av.right(90)

av.forward(90)

av.right(120)

av.forward(170)

av.right(150)

av.forward(150)

av.end_fill()
done()