from turtle import *

import utils


def draw_Traiangle(length=20):
    for i in range(3):
        forward(length)
        right(120)

Screen().colormode(255)
shape("turtle")
speed(0)
tracer(False)
#draw_square(100)
#draw_square(50)
#draw_square()
for i in range(1000):
    right(10)
    my_colour = utils.get_random_colour()
    fillcolor(my_colour)
    color(my_colour)
    #draw_Traiangle(i*2)
    draw_Traiangle(50)
done()