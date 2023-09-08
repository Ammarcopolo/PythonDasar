import turtle as tt

tt.speed(0)
tt.setup(800, 500)

tt.penup()
tt.goto(-400, 250)
tt.pendown()


tt.color("red")
tt.begin_fill()
tt.forward(800)
tt.right(90)
tt.forward(250)
tt.right(90)
tt.forward(800)
tt.end_fill()

tt.hideturtle()
tt.done()

