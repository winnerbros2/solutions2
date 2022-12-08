import turtle
turtle.bgcolor("white")
turtle.pencolor("black")
turtle.pensize(5)

for a in range(10, 500, 10):
  turtle.forward(a)
  turtle.left(90)

turtle.mainloop()


