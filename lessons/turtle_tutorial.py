"""Turtle Tutorial paint thing"""

# from turtle import [function_name]

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
#turtle_object_variable.method_name(leo)
i = 0
leo.penup()
leo.goto(-150,-100)
leo.pendown()
colormode(255)
leo.begin_fill()
while (i < 3):
    leo.forward(300)
    leo.color(100, 100, 100)
    leo.left(120)
    i = i + 1
leo.end_fill()
done()

bob: Turtle = Turtle()
bob.speed(9.99)