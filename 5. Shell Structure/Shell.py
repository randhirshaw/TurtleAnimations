from turtle import *
bgcolor('black')
speed(0)
hideturtle()
for i in range(120):
    color('red')
    circle(i)
    color('green')
    circle(i*0.9)
    color('orange')
    circle(i*0.7)
    color('yellow')
    circle(i*0.5)
    right(3)
#right(30)
    forward(3)
#forward(40)

done()