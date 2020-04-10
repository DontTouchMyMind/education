# Draw a smiley using the written circle and arc functions.
import turtle as t
from ex_12 import semicircle
from ex_10 import circle
import turtle as t

t.shape('turtle')
t.speed()
t.color('black')

# Body
t.penup()
t.goto(-200, 0)
t.pendown()
t.fillcolor('yellow')
t.begin_fill()
circle(5)
t.end_fill()

# Left eye
t.penup()
t.goto(-135, 60)
t.pendown()
t.fillcolor('blue')
t.begin_fill()
circle(0.5)
t.end_fill()

# Right eye
t.penup()
t.goto(-5, 60)
t.pendown()
t.fillcolor('blue')
t.begin_fill()
circle(0.5)
t.end_fill()

# Nose
t.penup()
t.goto(-60, 20)
t.pendown()
t.width(8)
t.seth(270)
t.forward(40)

# Smile
t.penup()
t.goto(15, -25)
t.pendown()
t.color('red')
t.width(10)
semicircle(2.5)
