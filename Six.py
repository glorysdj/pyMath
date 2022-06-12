import random
from turtle import *

Screen().colormode(255)

def angle_for_n(n):
    #print("n: " + str(n))
    sum = (n - 2) * 180
    #print("sum: "  + str(sum))
    avg = sum / n
    #print("avg: "  + str(avg))
    angle = 180 - avg
    #print("angle: "  + str(angle))
    return angle

def draw_for_n(n, length):
    r =random.randint(0, 255)
    g =random.randint(0, 255)
    b =random.randint(0, 255)
    color((r, g, b))
    fillcolor((r, g, b))
    for j in range(n):
        forward(length)
        right(angle_for_n(n))

shape("turtle")
for i in range(3, 100):
    draw_for_n(i, 10)


#for i in range(6):
#    forward(150)
#    right(60)



done()