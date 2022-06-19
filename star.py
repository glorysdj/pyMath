from turtle import *
import utils

def draw_star(n, length):
    angle = 180-(90-360/n)*2
    print(str(n),str(angle))
    for i in range(n):
        forward(length)
        right(angle)


Screen().colormode(255)
shape("turtle")
speed(0)
tracer(False)

#draw_star(9, 100)

for i in range(500):
    my_colour = utils.get_random_colour()
    fillcolor(my_colour)
    color(my_colour)
    draw_star(17, i*2)
    right(3.6)


done()