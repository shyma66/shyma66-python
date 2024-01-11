import time
import turtle
time.sleep(5)
pen = turtle.Turtle()
turtle.bgcolor("black")
pen.pencolor("purple")
pen.width(5)
pen.speed(10)
def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)
draw(pen,8,12)