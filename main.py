# 10 X 10
#
# 20 size
#
# space 50 pace

from colors import color_list
from turtle import Turtle, Screen
from random import choice

kachuwa = Turtle()
screen = Screen()

kachuwa.ht()
kachuwa.pu()
kachuwa.setpos(-300, -300)
# kachuwa.st()

# kachuwa.pensize(20)
screen.colormode(255)
for i in range(1, 101):
    # kachuwa.pencolor(choice(color_list))
    kachuwa.dot(20, choice(color_list))
    kachuwa.fd(50)
    if i % 10 == 0:
        kachuwa.left(90)
        kachuwa.forward(50)
        kachuwa.left(90)
        kachuwa.setx(-300)
        kachuwa.right(180)













screen.screensize(400, 400)

screen.exitonclick()
