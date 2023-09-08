import turtle

# set up the turtle screen and set the background color to white
screen = turtle.Screen ()
screen.bgcolor ("white")


# create a new tuerle  and set its speed to fasttest possible
pen = turtle.Turtle ()
pen.speed(0)

#set the fill color red 
pen.fillcolor("red")
pen.begin_fill()

#draw the circle with a radius of 100 pixel
pen.circle (100)

# end the fill and stop drawing
pen.end_fill ()
pen.hideturtle()

#keep the turtle window open until it is manually closed
turtle.done()