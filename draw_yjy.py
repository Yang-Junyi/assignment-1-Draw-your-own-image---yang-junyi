from turtle import *

def draw_yjy():
    import turtle as t
    t.pensize(5)
    t.pencolor('red')
    t.color('black','yellow')
    begin_fill()
    for i in range(5):
        forward(200)
        right(144)
    end_fill()
    exitonclick() 

print("----- I'll draw for you! ----")
draw_yjy()

