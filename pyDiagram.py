from turtle import *

import utils

Screen().colormode(255)
shape("turtle")
speed(0)
tracer(False)

for i in range(3, 1000):
    right(i)
    my_colour = utils.get_random_colour()
    fillcolor(my_colour)
    color(my_colour)
    #utils.draw_for_n(17, i*2)
    #utils.draw_for_n(i, 50)
    utils.draw_for_n(9, 50)
done()