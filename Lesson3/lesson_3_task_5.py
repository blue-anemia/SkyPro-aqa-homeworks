from turtle import *


def draw_head(t):
    t.circle(50)


def draw_ear(t):
    t.forward(50)
    t.left(120)
    t.forward(50)
    t.left(120)
    t.forward(50)
    t.left(120)


def draw_face(t):
    t.penup()
    t.goto(-20, 20)
    t.pendown()
    t.circle(5)
    t.penup()
    t.goto(20, 20)
    t.pendown()
    t.circle(5)
    t.penup()
    t.goto(0, 10)
    t.pendown()
    t.circle(5)


def draw_cat():
    t = Turtle()
    t.speed(5)

    t.penup()
    t.goto(0, -50)
    t.pendown()

    draw_head(t)

    t.penup()
    t.goto(-30, 50)
    t.pendown()
    draw_ear(t)

    t.penup()
    t.goto(30, 50)
    t.pendown()
    draw_ear(t)

    draw_face(t)

    t.hideturtle()
    done()


setup(800, 600)

draw_cat()

exitonclick()
mainloop()
